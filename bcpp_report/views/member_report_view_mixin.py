from bcpp_subject.models import SubjectVisit
from member.models import HouseholdMember, EnrollmentLoss


from ..constants import YEAR_1_SURVEY, YEAR_2_SURVEY, YEAR_3_SURVEY
from ..forms import MemberQueryReportForm


class MemberReportViewMixin:

    def enrollment_loss_count(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return EnrollmentLoss.objects.filter(
            household_member__survey_schedule__icontains=survey_schedule).count()

    def consented_members(self, survey_schedule=None, map_area=None):
        """Return a count of consented member for a survey.
        """
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return SubjectVisit.objects.filter(
            survey_schedule__icontains=survey_schedule).count()

    def ineligible_members(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule,
            enrollment_loss_completed=True).count()

    def eligible_present_not_consented(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule,
            present_today=True,
            eligible_subject=True).count()

    def undecided(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule,
            undecided=True).count()

    def refused(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule,
            refused=True).count()

    def absent(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule,
            absent=True).count()

    def htc(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule,
            htc=True).count()

    def refused_htc(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule,
            refused_htc=True).count()

    def total_members(self, survey_schedule=None, map_area=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
        return HouseholdMember.objects.filter(
            survey_schedule__icontains=survey_schedule).count()

    def member_report(self, map_area=None):

        year_1_report = {
            'Total Members': self.total_members(YEAR_1_SURVEY, map_area),
            'Eligible member, present not consented': self.eligible_present_not_consented(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Ineligible': self.ineligible_members(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Enrollment loss': self.enrollment_loss_count(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Undecided': self.undecided(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Refused': self.refused(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Absent': self.absent(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'HTC': self.htc(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Refused htc': self.refused_htc(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area),
            'Consented subjects': self.consented_members(
                survey_schedule=YEAR_1_SURVEY, map_area=map_area)}

        year_2_report = {
            'Total Members': self.total_members(YEAR_2_SURVEY, map_area),
            'Eligible member, present not consented': self.eligible_present_not_consented(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Members not eligibles': self.ineligible_members(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Enrollment loss': self.enrollment_loss_count(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Undecided': self.undecided(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Refused': self.refused(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Absent': self.absent(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'HTC': self.htc(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Refused htc': self.refused_htc(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area),
            'Consented subjects': self.consented_members(
                survey_schedule=YEAR_2_SURVEY, map_area=map_area)}

        year_3_report = {
            'Total Members': self.total_members(YEAR_3_SURVEY, map_area),
            'Eligible member, present not consented': self.eligible_present_not_consented(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Members not eligibles': self.ineligible_members(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Enrollment loss': self.enrollment_loss_count(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Undecided': self.undecided(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Refused': self.refused(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Absent': self.absent(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'HTC': self.htc(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Refused htc': self.refused_htc(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area),
            'Consented subjects': self.consented_members(
                survey_schedule=YEAR_3_SURVEY, map_area=map_area)}

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
