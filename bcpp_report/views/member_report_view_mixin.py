import os
import pandas as pd

from django.apps import apps as django_apps
from django.contrib import messages

from bcpp_report.forms import MemberQueryReportForm


class MemberReportViewMixin:

    def member_report(self, map_area=None):
        if map_area:
            pass
        members_hearder = django_apps.get_app_config(
            'bcpp_report').members_hearder
        members_file_path = django_apps.get_app_config(
            'bcpp_report').members_file_path
        if not os.path.exists(members_file_path):
            messages.add_message(
                self.request,
                messages.WARNING,
                'The file {0} does not exists, please generate report files first.'.format(members_file_path))
            return {}
        else:
            df = pd.read_csv(members_file_path, skipinitialspace=True, usecols=members_hearder)
            if map_area:
                df = df[(df.survey_schedule.str.contains(map_area, regex=True))]

            df_year_1 = df[df.survey_schedule.str.contains(
                'bcpp-survey.bcpp-year-1', regex=True)]
            df_year_2 = df[df.survey_schedule.str.contains(
                'bcpp-survey.bcpp-year-2', regex=True)]
            df_year_3 = df[df.survey_schedule.str.contains(
                'bcpp-survey.bcpp-year-3', regex=True)]

            year_1_report = {
                'Total Members': len(df_year_1),
                'Eligible members Not consented': len(
                    df_year_1[(df_year_1.eligible_member) &
                              (df_year_1.eligible_subject == False)]),
                'Members not eligibles': len(
                    df_year_1[df_year_1.eligible_member == False]),
                'Eligible member, present not consented': len(
                    df_year_1[(df_year_1.eligible_member) &
                              (df_year_1.present_today) &
                              (df_year_1.eligible_subject == False)]),
                'Enrollment loss': len(
                    df_year_1[df_year_1.enrollment_loss_completed == False]),
                'Undecided': len(df_year_1[df_year_1.undecided]),
                'Refused': len(df_year_1[df_year_1.refused]),
                'Absent': len(df_year_1[df_year_1.absent]),
                'HTC': len(df_year_1[df_year_1.htc]),
                'Refused htc': len(df_year_1[df_year_1.refused_htc]),
                'Consented subjects': len(df_year_1[df_year_1.eligible_subject])}

            year_2_report = {
                'Total Members': len(df_year_2),
                'Eligible members Not consented': len(
                    df_year_2[(df_year_2.eligible_member) &
                              (df_year_2.eligible_subject == False)]),
                'Members not eligibles': len(
                    df_year_2[df_year_2.eligible_member == False]),
                'Eligible member, present not consented': len(
                    df_year_2[(df_year_2.eligible_member) &
                              (df_year_2.present_today) &
                              (df_year_2.eligible_subject == False)]),
                'Enrollment los': len(
                    df_year_2[df_year_2.enrollment_loss_completed == False]),
                'Undecided': len(df_year_2[df_year_2.undecided]),
                'Refused': len(df_year_2[df_year_2.refused]),
                'Absent': len(df_year_2[df_year_2.absent]),
                'HTC': len(df_year_2[df_year_2.htc]),
                'Refused htc': len(df_year_2[df_year_2.refused_htc]),
                'Consented subjects': len(df_year_2[df_year_2.eligible_subject])}

            year_3_report = {
                'Total Members': len(df_year_3),
                'Eligible members Not consented': len(
                    df_year_3[(df_year_3.eligible_member) &
                              (df_year_3.eligible_subject == False)]),
                'Members not eligibles': len(
                    df_year_3[df_year_3.eligible_member == False]),
                'Eligible member, present not consented': len(
                    df_year_3[
                        (df_year_3.eligible_member) &
                        (df_year_3.present_today) &
                        (df_year_3.eligible_subject == False)]),
                'Enrollment los': len(
                    df_year_3[df_year_3.enrollment_loss_completed == False]),
                'Undecided': len(df_year_3[df_year_3.undecided]),
                'Refused': len(df_year_3[df_year_3.refused]),
                'Absent': len(df_year_3[df_year_3.absent]),
                'HTC': len(df_year_3[df_year_3.htc]),
                'Refused htc': len(df_year_3[df_year_3.refused_htc]),
                'Consented subjects': len(
                    df_year_3[df_year_3.eligible_subject])}

        return {
            'Year 1': year_1_report,
            'Year 2': year_2_report,
            'Year 3': year_3_report}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member_report_form = MemberQueryReportForm()
        if self.request.method == 'POST':
            household_report_form_instance = MemberQueryReportForm(
                self.request.POST)
            if household_report_form_instance.is_valid():
                map_area = household_report_form_instance.data.get('map_area')
                member_report = self.member_report(map_area)
                context.update(
                    member_report=member_report,
                    map_area=map_area)
        else:
            context.update(member_report=self.member_report())
        context.update(member_report_form=member_report_form)
        return context
