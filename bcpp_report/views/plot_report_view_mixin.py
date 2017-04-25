import os
import pandas as pd

from django.apps import apps as django_apps
from django.contrib import messages
from django.views.generic.edit import FormView

from plot.constants import (
    NON_RESIDENTIAL, RESIDENTIAL_NOT_HABITABLE,
    RESIDENTIAL_HABITABLE, INACCESSIBLE)

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

    def plot_report(self, map_area=None):
        plots_file_path = django_apps.get_app_config(
            'bcpp_report').plots_file_path
        plot_header = django_apps.get_app_config(
            'bcpp_report').plot_header
        if not os.path.exists(plots_file_path):
            messages.add_message(
                self.request,
                messages.WARNING,
                'The file {0} does not exists, please generate '
                'report files first.'.format(plots_file_path))
            return {}
        else:
            df = pd.read_csv(
                plots_file_path, skipinitialspace=True, usecols=plot_header)
            if map_area:
                df = df[(
                    df.map_area.str.contains(map_area, regex=True, na=False))]

            return {
                'Total plots': len(df),
                'Total Ess plots': len(df[df.rss == False]),
                'Confirmed plots': len(df[df.confirmed]),
                'Confirmed Ess plots': len(df[(
                    df.confirmed) & (df.rss == False)]),
                'Not confirmed plots': len(df[df.confirmed == False]),
                'Not confirmed Ess plots': len(
                    df[(df.confirmed == False) & (df.rss == False)]),
                'Enrolled Plots': len(df[df.enrolled]),
                'Enrolled Ess Plots': len(df[(
                    df.enrolled) & (df.rss == False)]),
                'Accessible': len(df[df.accessible]),
                'In accessible': len(df[(
                    df.status.str.contains(INACCESSIBLE,
                                           regex=True, na=False))]),
                'Accessible Ess plots attempts 1': len(
                    df[(df.access_attempts == 1) & (df.rss == False)]),
                'Accessible Ess plots attempts 2': len(
                    df[(df.access_attempts == 2) & (df.rss == False)]),
                'Accessible Ess plots attempts 3 plus': len(
                    df[(df.access_attempts >= 3) & (df.rss == False)]),
                'Residential habitable': len(
                    df[(df.status.str.contains(
                        RESIDENTIAL_HABITABLE, regex=True, na=False))]),
                'Residential habitable Ess': len(
                    df[(df.status.str.contains(
                        RESIDENTIAL_HABITABLE,
                        regex=True, na=False)) & (df.rss == False)]),
                'Residential not habitable': len(
                    df[(df.status.str.contains(
                        RESIDENTIAL_NOT_HABITABLE, regex=True, na=False))]),
                'Residential not habitable Ess': len(
                    df[(df.status.str.contains(
                        RESIDENTIAL_NOT_HABITABLE,
                        regex=True, na=False)) & (df.rss == False)]),
                'Non residential': len(df[(
                    df.status.str.contains(NON_RESIDENTIAL,
                                           regex=True, na=False))]),
                'Non residential': len(
                    df[(df.status.str.contains(
                        NON_RESIDENTIAL,
                        regex=True, na=False)) & (df.rss == False)])}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(plot_report=self.plot_report())
        return context
