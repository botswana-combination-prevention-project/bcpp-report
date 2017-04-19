from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from edc_base.view_mixins import EdcBaseViewMixin

from .utils import report_files
from ..forms import GenerateCommunityReportForm


class HomeView(EdcBaseViewMixin, TemplateView, FormView):

    form_class = GenerateCommunityReportForm
    app_config_name = 'bcpp_report'
    template_name = 'bcpp_report/home_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(report_files=report_files())
        return context
