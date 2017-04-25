from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin

from .household_report_view_mixin import HouseholdReportViewMixin
from .member_report_view_mixin import MemberReportViewMixin
from .plot_report_view_mixin import PlotReportViewMixin
from .requisition_report_view_mixin import RequisitionReportViewMixin


class HomeView(EdcBaseViewMixin, PlotReportViewMixin, HouseholdReportViewMixin,
               MemberReportViewMixin, RequisitionReportViewMixin, TemplateView):

    app_config_name = 'bcpp_report'
    template_name = 'bcpp_report/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(map_area=None)
        return context
