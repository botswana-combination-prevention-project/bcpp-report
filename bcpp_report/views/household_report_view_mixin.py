import os
import pandas as pd

from django.apps import apps as django_apps
from django.contrib import messages

from ..forms import HouseholdQueryReportForm


class HouseholdReportViewMixin:

    def household_report(self, map_area=None):
        household_structure_header = django_apps.get_app_config(
            'bcpp_report').household_structure_header
        household_structures_file_path = django_apps.get_app_config(
            'bcpp_report').household_structures_file_path
        if not os.path.exists(household_structures_file_path):
            messages.add_message(
                self.request,
                messages.WARNING,
                'The file {0} does not exists, please generate report files first.'.format(household_structures_file_path))
            return {}
        else:
            df = pd.read_csv(
                household_structures_file_path,
                skipinitialspace=True,
                usecols=household_structure_header)
            if map_area:
                df = df[(df.survey_schedule.str.contains(map_area, regex=True))]

            #  Build data frames for different years for household structure
            df_year_1_hs = df[df.survey_schedule.str.contains(
                'bcpp-survey.bcpp-year-1', regex=True)]
            df_year_2_hs = df[df.survey_schedule.str.contains(
                'bcpp-survey.bcpp-year-2', regex=True)]
            df_year_3_hs = df[df.survey_schedule.str.contains(
                'bcpp-survey.bcpp-year-3', regex=True)]

            year_1_report = {
                'Total Households': len(df_year_1_hs),
                'Enumerated': len(df_year_1_hs[df_year_1_hs.enumerated]),
                'Not enumerated': len(df_year_1_hs[df_year_1_hs.enumerated == False]),
                'Failled enumeration attempts 1 times': len(
                    df_year_1_hs[df_year_1_hs.enumeration_attempts == 1]),
                'Failled enumeration attempts 2 times': len(
                    df_year_1_hs[df_year_1_hs.enumeration_attempts == 2]),
                'Failled enumeration attempts 3 times': len(
                    df_year_1_hs[df_year_1_hs.enumeration_attempts == 3]),
                'Enrolled households': len(df_year_1_hs[df_year_1_hs.enrolled]),
                'Not enrolled': len(df_year_1_hs[df_year_1_hs.enrolled == False]),
                'No iligible members': len(
                    df_year_1_hs[df_year_1_hs.eligible_members == False]),
                'Refused enumeration': len(
                    df_year_1_hs[df_year_1_hs.refused_enumeration])}

            year_2_report = {
                'Total Households': len(df_year_2_hs),
                'Enumerated': len(df_year_2_hs[df_year_2_hs.enumerated]),
                'Not enumerated': len(df_year_2_hs[df_year_2_hs.enumerated == False]),
                'Failled enumeration attempts 1 times': len(
                    df_year_2_hs[df_year_2_hs.enumeration_attempts == 1]),
                'Failled enumeration attempts 2 times': len(
                    df_year_2_hs[df_year_2_hs.enumeration_attempts == 2]),
                'Failled enumeration attempts 3 times': len(
                    df_year_2_hs[df_year_2_hs.enumeration_attempts == 3]),
                'Enrolled households': len(df_year_2_hs[df_year_2_hs.enrolled]),
                'Not enrolled': len(df_year_2_hs[df_year_2_hs.enrolled == False]),
                'No iligible members': len(
                    df_year_2_hs[df_year_2_hs.eligible_members == False]),
                'Refused enumeration': len(
                    df_year_2_hs[df_year_2_hs.refused_enumeration])}

            year_3_report = {
                'Total Households': len(df_year_3_hs),
                'Enumerated': len(df_year_3_hs[df_year_3_hs.enumerated]),
                'Not enumerated': len(df_year_3_hs[df_year_3_hs.enumerated == False]),
                'Failled enumeration attempts 1 times': len(
                    df_year_3_hs[df_year_3_hs.enumeration_attempts == 1]),
                'Failled enumeration attempts 2 times': len(
                    df_year_3_hs[df_year_3_hs.enumeration_attempts == 2]),
                'Failled enumeration attempts 3 times': len(
                    df_year_3_hs[df_year_3_hs.enumeration_attempts == 3]),
                'Enrolled households': len(df_year_3_hs[df_year_3_hs.enrolled]),
                'Not enrolled': len(df_year_3_hs[df_year_3_hs.enrolled == False]),
                'No iligible members': len(
                    df_year_3_hs[df_year_3_hs.eligible_members == False]),
                'Refused enumeration': len(
                    df_year_3_hs[df_year_3_hs.refused_enumeration])}

        return {'Year 1': year_1_report, 'Year 2': year_2_report, 'Year 3': year_3_report}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        household_report_form = HouseholdQueryReportForm()
        if self.request.method == 'POST':
            household_report_form_instance = HouseholdQueryReportForm(
                self.request.POST)
            if household_report_form_instance.is_valid():
                map_area = household_report_form_instance.data.get('map_area')
                household_report = self.household_report(map_area)
                context.update(
                    household_report=household_report,
                    map_area=map_area)
        else:
            context.update(household_report=self.household_report())
        context.update(household_report_form=household_report_form)
        return context
