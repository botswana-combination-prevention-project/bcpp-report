from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from edc_base.view_mixins import EdcBaseViewMixin

from household.models import HouseholdStructure
from member.models import HouseholdMember

from bcpp_subject.models import SubjectRequisition

from plot.models import Plot

from .utils import dump, report_files
from ..models import ReportFile
from ..forms import GenerateCommunityReportForm


class GenerateReportFiles(EdcBaseViewMixin, TemplateView, FormView):

    form_class = GenerateCommunityReportForm
    app_config_name = 'bcpp_report'
    template_name = 'bcpp_report/home_view.html'

    def form_valid(self, form):
        context = self.get_context_data(**self.kwargs)
        if form.is_valid():
            map_area = form.cleaned_data.get('map_area')
            self.generate_reports_files(map_area)
            context.update(report_files=report_files())
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def generate_reports_files(self, map_area=None):
        """Generates csv files to be used for reports.
        """

        #  Delete exisiting file records.
        ReportFile.objects.all().delete()

        #  Generate plot report file
        plots_qs = Plot.objects.all()
        household_Structure_qs = HouseholdStructure.objects.all()
        member_qs = HouseholdMember.objects.all()
        requisition_qs = SubjectRequisition.objects.all()
        if map_area:
            plots_qs = Plot.objects.filter(map_area=map_area)
            household_Structure_qs = HouseholdStructure.objects.filter(
                household__plot__map_area=map_area)
            member_qs = HouseholdMember.objects.filter(
                household_structure__household__plot__map_area=map_area)
            requisition_qs = SubjectRequisition.objects.filter(
                subject_visit__household_member__household_structure__household__plot__map_area=map_area)
        else:
            map_area = 'All Communities'

        plot_hearder = django_apps.get_app_config(
            'bcpp_report').plot_hearder
        plots_file_path = django_apps.get_app_config(
            'bcpp_report').plots_file_path
        dump(plots_qs, plot_hearder, plots_file_path)
        ReportFile.objects.create(name=plots_file_path, map_area=map_area)

        #  Generate household structure report file
        household_strucuture_hearder = django_apps.get_app_config(
            'bcpp_report').household_strucuture_hearder
        household_structures_file_path = django_apps.get_app_config(
            'bcpp_report').household_structures_file_path
        dump(
            household_Structure_qs,
            household_strucuture_hearder,
            household_structures_file_path)
        ReportFile.objects.create(
            name=household_structures_file_path, map_area=map_area)

        #  Generate household member report file
        members_hearder = django_apps.get_app_config(
            'bcpp_report').members_hearder
        members_file_path = django_apps.get_app_config(
            'bcpp_report').members_file_path
        dump(member_qs, members_hearder, members_file_path)
        ReportFile.objects.create(name=members_file_path, map_area=map_area)

        #  Generate subject requisition report file
        requisition_header = django_apps.get_app_config(
            'bcpp_report').requisition_header
        requisitions_file_path = django_apps.get_app_config(
            'bcpp_report').requisitions_file_path
        dump(requisition_qs, requisition_header, requisitions_file_path)
        ReportFile.objects.create(name=requisitions_file_path, map_area=map_area)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('generate') == 'all':
            self.generate_reports_files()
        context.update(report_files=report_files())
        return context
