import os
import pandas as pd

from django.apps import apps as django_apps
from django.contrib import messages

from edc_constants.constants import YES, NO

from bcpp_subject.constants import MICROTUBE, RESEARCH_BLOOD_DRAW, VENOUS, VIRAL_LOAD, POC_VIRAL_LOAD

from ..forms import RequisitionQueryReportForm


class RequisitionReportViewMixin:

    def requisition_report(self, study_site_name=None, start_date=None, end_date=None):
        requisition_header = django_apps.get_app_config(
            'bcpp_report').requisition_header
        requisition_header.append('survey_schedule')
        requisitions_file_path = django_apps.get_app_config(
            'bcpp_report').requisitions_file_path
        if not os.path.exists(requisitions_file_path):
            messages.add_message(
                self.request,
                messages.WARNING,
                'The file {0} does not exists, please generate report files first.'.format(requisitions_file_path))
            return {}
        else:
            df = pd.read_csv(
                requisitions_file_path,
                skipinitialspace=True,
                usecols=requisition_header)
            if study_site_name:
                df = df[(df.study_site_name.str.contains(study_site_name, regex=True, na=False))]
            if start_date and end_date:
                #  Re-format dates
                start_date = start_date.split('/')
                start_date = start_date[2] + '-' + start_date[1] + '-' + start_date[0] + ' 00:00:00+00:00'
                end_date = end_date.split('/')
                end_date = end_date[2] + '-' + end_date[1] + '-' + end_date[0] + ' 00:00:00+00:00'

                df = df[
                    (df['requisition_datetime'] > start_date) &
                    (df['requisition_datetime'] <= end_date)]

            df_year_1_requisitions = df[df.survey_schedule.str.contains('bcpp-survey.bcpp-year-1', regex=True, na=False)]
            df_year_2_requisitions = df[df.survey_schedule.str.contains('bcpp-survey.bcpp-year-2', regex=True, na=False)]
            df_year_3_requisitions = df[df.survey_schedule.str.contains('bcpp-survey.bcpp-year-3', regex=True, na=False)]

        return [
            self.report_per_panel(df_year_1_requisitions),
            self.report_per_panel(df_year_2_requisitions),
            self.report_per_panel(df_year_3_requisitions)]

    def report_per_panel(self, df):

        df_microtube = df[
            (df.panel_name.str.contains(MICROTUBE, regex=True, na=False))]
        df_rbd = df[(df.panel_name.str.contains(
            RESEARCH_BLOOD_DRAW, regex=True, na=False))]
        df_venous = df[(df.panel_name.str.contains(
            VENOUS, regex=True, na=False))]
        df_vl = df[(df.panel_name.str.contains(
            VIRAL_LOAD, regex=True, na=False))]
        df_poc_vl = df[(df.panel_name.str.contains(
            POC_VIRAL_LOAD, regex=True, na=False))]

        microtube = {
            'Total Requisitions': len(df_microtube),
            'Drawn': len(df_microtube[
                (df_microtube.is_drawn.str.contains(
                    YES, regex=True, na=False))]),
            'Not Drawn': len(df_microtube[
                (df_microtube.is_drawn.str.contains(
                    NO, regex=True, na=False))]),
            'Recieved': len(df_microtube[df_microtube.received]),
            'Not Recieved': len(df_microtube[df_microtube.received == False]),
            'Processed': len(df_microtube[df_microtube.processed]),
            'Not Processed': len(df_microtube[df_microtube.processed == False]),
            'Packed': len(df_microtube[df_microtube.packed]),
            'Not Packed': len(df_microtube[df_microtube.packed == False]),
            'Shipped': len(df_microtube[df_microtube.shipped]),
            'Not Shipped': len(df_microtube[df_microtube.shipped == False])}

        venous = {
            'Total Requisitions': len(df_venous),
            'Drawn': len(df_venous[
                (df_venous.is_drawn.str.contains(YES, regex=True, na=False))]),
            'Not Drawn': len(df_venous[
                (df_venous.is_drawn.str.contains(NO, regex=True, na=False))]),
            'Recieved': len(df_venous[df_venous.received]),
            'Not Recieved': len(df_venous[df_venous.received == False]),
            'Processed': len(df_venous[df_venous.processed]),
            'Not Processed': len(df_venous[df_venous.processed == False]),
            'Packed': len(df_venous[df_venous.packed]),
            'Not Packed': len(df_venous[df_venous.packed == False]),
            'Shipped': len(df_venous[df_venous.shipped]),
            'Not Shipped': len(df_venous[df_venous.shipped == False])}

        rbd = {
            'Total Requisitions': len(df_rbd),
            'Drawn': len(df_rbd[(
                df_rbd.is_drawn.str.contains(YES, regex=True, na=False))]),
            'Not Drawn': len(df_rbd[
                (df_rbd.is_drawn.str.contains(NO, regex=True, na=False))]),
            'Recieved': len(df_rbd[df_rbd.received]),
            'Not Recieved': len(df_rbd[df_rbd.received == False]),
            'Processed': len(df_rbd[df_rbd.processed]),
            'Not Processed': len(df_rbd[df_rbd.processed == False]),
            'Packed': len(df_rbd[df_rbd.packed]),
            'Not Packed': len(df_rbd[df_rbd.packed == False]),
            'Shipped': len(df_rbd[df_rbd.shipped]),
            'Not Shipped': len(df_rbd[df_rbd.shipped == False])}

        poc_vl = {
            'Total Requisitions': len(df_poc_vl),
            'Drawn': len(df_poc_vl[
                (df_poc_vl.is_drawn.str.contains(YES, regex=True, na=False))]),
            'Not Drawn': len(df_poc_vl[
                (df_poc_vl.is_drawn.str.contains(NO, regex=True, na=False))]),
            'Recieved': len(df_poc_vl[df_poc_vl.received]),
            'Not Recieved': len(df_poc_vl[df_poc_vl.received == False]),
            'Processed': len(df_poc_vl[df_poc_vl.processed]),
            'Not Processed': len(df_poc_vl[df_poc_vl.processed == False]),
            'Packed': len(df_poc_vl[df_poc_vl.packed]),
            'Not Packed': len(df_poc_vl[df_poc_vl.packed == False]),
            'Shipped': len(df_poc_vl[df_poc_vl.shipped]),
            'Not Shipped': len(df_poc_vl[df_poc_vl.shipped == False])}

        viral_load = {
            'Total Requisitions': len(df_vl),
            'Drawn': len(df_vl[(df_vl.is_drawn.str.contains(YES, regex=True, na=False))]),
            'Not Drawn': len(df_vl[(df_vl.is_drawn.str.contains(NO, regex=True, na=False))]),
            'Recieved': len(df_vl[df_vl.received]),
            'Not Recieved': len(df_vl[df_vl.received == False]),
            'Processed': len(df_vl[df_vl.processed]),
            'Not Processed': len(df_vl[df_vl.processed == False]),
            'Packed': len(df_vl[df_vl.packed]),
            'Not Packed': len(df_vl[df_vl.packed == False]),
            'Shipped': len(df_vl[df_vl.shipped]),
            'Not Shipped': len(df_vl[df_vl.shipped == False])}

        return {
            'Microtube': microtube,
            'RBD': rbd,
            'Venous': venous,
            'Virul Load': viral_load,
            'POC VL': poc_vl}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        requisition_report_form = RequisitionQueryReportForm()
        if self.request.method == 'POST':
            requisition_report_form_instance = RequisitionQueryReportForm(
                self.request.POST)
            if requisition_report_form_instance.is_valid():
                map_area = requisition_report_form_instance.data.get('map_area')
                start_date = requisition_report_form_instance.data.get('start_date')
                end_end = requisition_report_form_instance.data.get('end_end')
                requisition_report = self.requisition_report(
                    study_site_name=map_area,
                    start_date=start_date,
                    end_date=end_end)
                context.update(
                    requisition_report=requisition_report,
                    map_area=map_area)
        else:
            context.update(requisition_report=self.requisition_report())
        context.update(requisition_report_form=requisition_report_form)
        return context
