import os
import pandas as pd

from django.apps import apps as django_apps
from django.contrib import messages

from household.models import HouseholdStructure

from ..constants import YEAR_1_SURVEY, YEAR_2_SURVEY, YEAR_3_SURVEY
from ..forms import HouseholdQueryReportForm


class HouseholdReportViewMixin:

    def total_households(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule).count()

    def enumerated(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enumerated=True).count()

    def not_enumerated(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enumerated=False).count()

    def enumeration_attempts_once(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enumeration_attempts=1).count()

    def enumeration_attempts_twice(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enumeration_attempts=2).count()

    def enumeration_attempts_three_or_more(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enumeration_attempts__gte=2).count()

    def enrolled(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enrolled=True).count()

    def not_enrolled(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enrolled=False).count()

    def no_eligible_members(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            eligible_members=False).count()

    def refused_enumeration(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdStructure.objects.filter(
            survey_schedule__icontains=survey_schedule,
            refused_enumeration=True).count()

    def household_report(self, map_area=None):

        year_1_report = {
            'Total Households': self.total_households(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Enumerated': self.enumerated(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Not enumerated': self.not_enumerated(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Failled enumeration attempts 1 times': self.enumeration_attempts_once(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Failled enumeration attempts 2 times': self.enumeration_attempts_twice(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Failled enumeration attempts 3 times': self.enumeration_attempts_three_or_more(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Enrolled households': self.enrolled(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Not enrolled': self.not_enrolled(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'No iligible members': self.no_eligible_members(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Refused enumeration': self.refused_enumeration(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area)}

        year_2_report = {
            'Total Households': self.total_households(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Enumerated': self.enumerated(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Not enumerated': self.not_enumerated(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Failled enumeration attempts 1 times': self.enumeration_attempts_once(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Failled enumeration attempts 2 times': self.enumeration_attempts_twice(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Failled enumeration attempts 3 times': self.enumeration_attempts_three_or_more(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Enrolled households': self.enrolled(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Not enrolled': self.not_enrolled(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'No iligible members': self.no_eligible_members(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Refused enumeration': self.refused_enumeration(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area)}

        year_3_report = {
            'Total Households': self.total_households(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Enumerated': self.enumerated(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Not enumerated': self.not_enumerated(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Failled enumeration attempts 1 times': self.enumeration_attempts_once(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Failled enumeration attempts 2 times': self.enumeration_attempts_twice(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Failled enumeration attempts 3 times': self.enumeration_attempts_three_or_more(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Enrolled households': self.enrolled(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Not enrolled': self.not_enrolled(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'No iligible members': self.no_eligible_members(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Refused enumeration': self.refused_enumeration(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area)}

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
