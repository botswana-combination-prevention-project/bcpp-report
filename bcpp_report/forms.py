from django import forms

from functools import partial

from .choices import MAP_AREAS

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class PlotQueryReportForm(forms.Form):

    map_area = forms.ChoiceField(
        choices=MAP_AREAS,
        required=False,
        label='Map Area',
        initial='option_one')


class HouseholdQueryReportForm(forms.Form):

    map_area = forms.ChoiceField(
        choices=MAP_AREAS,
        required=False,
        label='Map Area',
        initial='option_one')


class MemberQueryReportForm(forms.Form):

    map_area = forms.ChoiceField(
        choices=MAP_AREAS,
        required=False,
        label='Map Area',
        initial='option_one')


class RequisitionQueryReportForm(forms.Form):

    map_area = forms.ChoiceField(
        choices=MAP_AREAS,
        required=False,
        label='Study site name',
        initial='option_one')
    start_date = forms.DateField(label='Start date', required=False, widget=DateInput())
    end_end = forms.DateField(label='End date', required=False, widget=DateInput())


class GenerateCommunityReportForm(forms.Form):

    map_area = forms.ChoiceField(
        choices=MAP_AREAS,
        required=False,
        label='Community',
        initial='option_one')
