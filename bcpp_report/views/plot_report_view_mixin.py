from django.views.generic.edit import FormView

from plot.constants import NON_RESIDENTIAL, RESIDENTIAL_NOT_HABITABLE
from plot.constants import RESIDENTIAL_HABITABLE
from plot.models import Plot

from ..forms import PlotQueryReportForm


class PlotReportViewMixin(FormView):

    form_class = PlotQueryReportForm

    def form_valid(self, form):
        context = self.get_context_data(**self.kwargs)
        if form.is_valid():
            map_area = form.cleaned_data.get('map_area')
            context.update(
                plot_report=self.plot_report(map_area),
                map_area=map_area)
        return self.render_to_response(context)

    def total_plots(self, map_area=None):
        if map_area:
            return Plot.objects.filter(map_area=map_area).count()
        return Plot.objects.all().count()

    def total_ess_plots(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                rss=False).count()
        return Plot.objects.filter(rss=False).count()

    def confirmed(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                confirmed=True).count()
        return Plot.objects.filter(confirmed=True).count()

    def ess_confirmed(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                confirmed=True,
                rss=False).count()
        return Plot.objects.filter(confirmed=True, rss=False).count()

    def not_confirmed(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                confirmed=False).count()
        return Plot.objects.filter(confirmed=False).count()

    def ess_not_confirmed(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                confirmed=False,
                rss=False).count()
        return Plot.objects.filter(confirmed=False, rss=False).count()

    def ess_enrolled_plots(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                enrolled=True,
                rss=False).count()
        return Plot.objects.filter(enrolled=True, rss=False).count()

    def enrolled_plots(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                enrolled=True).count()
        return Plot.objects.filter(enrolled=True).count()

    def accessible_plots(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                accessible=True).count()
        return Plot.objects.filter(accessible=True).count()

    def inaccessible_plots(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                accessible=False).count()
        return Plot.objects.filter(accessible=False).count()

    def ess_accessible_plots(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                accessible=True,
                rss=False).count()
        return Plot.objects.filter(accessible=True, rss=False).count()

    def ess_access_attempts_once(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                access_attempts=1,
                rss=False).count()
        return Plot.objects.filter(access_attempts=1, rss=False).count()

    def ess_access_attempts_twice(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                access_attempts=2,
                rss=False).count()
        return Plot.objects.filter(access_attempts=2, rss=False).count()

    def ess_access_attempts_3_or_more(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                access_attempts__gte=3,
                rss=False).count()
        return Plot.objects.filter(access_attempts__gte=3, rss=False).count()

    def residential_habitable(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                status=RESIDENTIAL_HABITABLE).count()
        return Plot.objects.filter(
            status=RESIDENTIAL_HABITABLE).count()

    def ess_residential_habitable(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                status=RESIDENTIAL_HABITABLE,
                rss=False).count()
        return Plot.objects.filter(
            status=RESIDENTIAL_HABITABLE, rss=False).count()

    def residential_not_habitable(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                status=RESIDENTIAL_NOT_HABITABLE).count()
        return Plot.objects.filter(status=RESIDENTIAL_NOT_HABITABLE).count()

    def ess_residential_not_habitable(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                status=RESIDENTIAL_NOT_HABITABLE,
                rss=False).count()
        return Plot.objects.filter(
            status=RESIDENTIAL_NOT_HABITABLE, rss=False).count()

    def non_residential(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                status=NON_RESIDENTIAL).count()
        return Plot.objects.filter(status=NON_RESIDENTIAL).count()

    def ess_non_residential(self, map_area=None):
        if map_area:
            return Plot.objects.filter(
                map_area=map_area,
                status=NON_RESIDENTIAL,
                rss=False).count()
        return Plot.objects.filter(
            status=NON_RESIDENTIAL, rss=False).count()

    def plot_report(self, map_area=None):

        return {
            'Total plots': self.total_plots(map_area),
            'Total Ess plots': self.total_ess_plots(map_area),
            'Confirmed plots': self.confirmed(map_area),
            'Confirmed Ess plots': self.ess_confirmed(map_area),
            'Not confirmed plots': self.not_confirmed(map_area),
            'Not confirmed Ess plots': self.ess_not_confirmed(map_area),
            'Enrolled Plots': self.enrolled_plots(map_area),
            'Enrolled Ess Plots': self.ess_enrolled_plots(map_area),
            'Accessible': self.accessible_plots(map_area),
            'In accessible': self.inaccessible_plots(map_area),
            'Accessible Ess plots attempts 1': self.ess_access_attempts_once(map_area),
            'Accessible Ess plots attempts 2': self.ess_access_attempts_twice(map_area),
            'Accessible Ess plots attempts 3 plus': self.ess_access_attempts_3_or_more(map_area),
            'Residential habitable': self.residential_habitable(map_area),
            'Residential habitable Ess': self.ess_residential_habitable(map_area),
            'Residential not habitable': self.residential_not_habitable(map_area),
            'Residential not habitable Ess': self.ess_residential_not_habitable(map_area),
            'Non residential': self.non_residential(map_area),
            'Non residential Ess': self.ess_non_residential(map_area)}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(plot_report=self.plot_report())
        return context
