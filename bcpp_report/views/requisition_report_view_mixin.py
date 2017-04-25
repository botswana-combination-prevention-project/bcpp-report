from datetime import datetime

from bcpp_subject.constants import (
    MICROTUBE, RESEARCH_BLOOD_DRAW, VENOUS, VIRAL_LOAD, ELISA)
from bcpp_subject.models import SubjectRequisition

from ..forms import RequisitionQueryReportForm
from ..constants import YEAR_1_SURVEY, YEAR_2_SURVEY, YEAR_3_SURVEY


class RequisitionReportViewMixin:

    def total_requisitions(self, panel_name=None, survey_schedule=None,
                           map_area=None, start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def is_drawn(self, panel_name=None, survey_schedule=None, map_area=None,
                 start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    is_drawn=True,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    is_drawn=True).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            is_drawn=True,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def not_drawn(self, panel_name=None, survey_schedule=None, map_area=None,
                  start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    is_drawn=False).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    is_drawn=False).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            is_drawn=False,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def received(self, panel_name=None, survey_schedule=None, map_area=None,
                 start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    received=True,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    received=True).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            received=True,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def not_received(self, panel_name=None, survey_schedule=None, map_area=None,
                     start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    received=False).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    received=False).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            received=False,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def processed(self, panel_name=None, survey_schedule=None, map_area=None,
                  start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    processed=True).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    processed=True).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            processed=True,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def not_processed(self, panel_name=None, survey_schedule=None,
                      map_area=None, start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    processed=False,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    processed=False).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            processed=False,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def packed(self, panel_name=None, survey_schedule=None, map_area=None,
               start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    packed=True,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    packed=True).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            packed=True,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def not_packed(self, panel_name=None, survey_schedule=None, map_area=None,
                   start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    packed=False,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    packed=False).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            packed=False,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def shipped(self, panel_name=None, survey_schedule=None, map_area=None,
                start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    shipped=True,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    shipped=True).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            shipped=True,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def not_shipped(self, panel_name=None, survey_schedule=None, map_area=None,
                    start_date=None, end_date=None):
        if map_area and survey_schedule:
            survey_schedule = survey_schedule + '.' + map_area
            if start_date and end_date:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    shipped=False,
                    requisition_datetime__lte=end_date,
                    requisition_datetime__gte=start_date).count()
            else:
                return SubjectRequisition.objects.filter(
                    panel_name=panel_name,
                    subject_visit__survey_schedule__icontains=survey_schedule,
                    shipped=False).count()
        return SubjectRequisition.objects.filter(
            panel_name=panel_name,
            shipped=False,
            subject_visit__survey_schedule__icontains=survey_schedule).count()

    def requisition_per_panel_name(self, panel_name=None, survey_schedule=None,
                                   map_area=None, start_date=None,
                                   end_date=None):
        return {
            'Total Requisitions': self.total_requisitions(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Drawn': self.is_drawn(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Not Drawn': self.not_drawn(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Received': self.received(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Not Received': self.not_received(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Processed': self.processed(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Not Processed': self.not_processed(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Packed': self.packed(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Not Packed': self.not_packed(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Shipped': self.shipped(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'Not Shipped': self.not_shipped(
                panel_name=panel_name, survey_schedule=survey_schedule,
                map_area=map_area, start_date=start_date, end_date=end_date)}

    def requisition_report(self, map_area=None, start_date=None, end_date=None):

        year_1 = {
            'MICROTUBE': self.requisition_per_panel_name(
                panel_name=MICROTUBE, survey_schedule=YEAR_1_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'VENOUS': self.requisition_per_panel_name(
                panel_name=VENOUS, survey_schedule=YEAR_1_SURVEY, map_area=map_area,
                start_date=start_date, end_date=end_date),
            'RESEARCH BLOOD DRAW': self.requisition_per_panel_name(
                panel_name=RESEARCH_BLOOD_DRAW, survey_schedule=YEAR_1_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'VIRAL LOAD': self.requisition_per_panel_name(
                panel_name=VIRAL_LOAD, survey_schedule=YEAR_1_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'ELISA': self.requisition_per_panel_name(
                panel_name=ELISA, survey_schedule=YEAR_1_SURVEY, map_area=map_area,
                start_date=start_date, end_date=end_date)}

        year_2 = {
            'MICROTUBE': self.requisition_per_panel_name(
                panel_name=MICROTUBE, survey_schedule=YEAR_2_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'VENOUS': self.requisition_per_panel_name(
                panel_name=VENOUS, survey_schedule=YEAR_2_SURVEY, map_area=map_area,
                start_date=start_date, end_date=end_date),
            'RESEARCH BLOOD DRAW': self.requisition_per_panel_name(
                panel_name=RESEARCH_BLOOD_DRAW, survey_schedule=YEAR_2_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'VIRAL LOAD': self.requisition_per_panel_name(
                panel_name=VIRAL_LOAD, survey_schedule=YEAR_2_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'ELISA': self.requisition_per_panel_name(
                panel_name=ELISA, survey_schedule=YEAR_2_SURVEY, map_area=map_area,
                start_date=start_date, end_date=end_date)}

        year_3 = {
            'MICROTUBE': self.requisition_per_panel_name(
                panel_name=MICROTUBE, survey_schedule=YEAR_3_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'VENOUS': self.requisition_per_panel_name(
                panel_name=VENOUS, survey_schedule=YEAR_3_SURVEY, map_area=map_area,
                start_date=start_date, end_date=end_date),
            'RESEARCH BLOOD DRAW': self.requisition_per_panel_name(
                panel_name=RESEARCH_BLOOD_DRAW, survey_schedule=YEAR_3_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'VIRAL LOAD': self.requisition_per_panel_name(
                panel_name=VIRAL_LOAD, survey_schedule=YEAR_3_SURVEY,
                map_area=map_area, start_date=start_date, end_date=end_date),
            'ELISA': self.requisition_per_panel_name(
                panel_name=ELISA, survey_schedule=YEAR_3_SURVEY, map_area=map_area,
                start_date=start_date, end_date=end_date)}

        return [year_1, year_2, year_3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        requisition_report_form = RequisitionQueryReportForm()
        if self.request.method == 'POST':
            requisition_report_form_instance = RequisitionQueryReportForm(
                self.request.POST)
            if requisition_report_form_instance.is_valid():
                map_area = requisition_report_form_instance.data.get(
                    'map_area')
                start_date = requisition_report_form_instance.data.get(
                    'start_date')
                if start_date:
                    start_date = datetime.strptime(start_date, '%m/%d/%Y')
                end_date = requisition_report_form_instance.data.get('end_end')
                if end_date:
                    end_date = datetime.strptime(end_date, '%m/%d/%Y')
                self.requisition_report(map_area, start_date, end_date)
                requisition_report = self.requisition_report(
                    map_area=map_area,
                    start_date=start_date,
                    end_date=end_date)
                context.update(
                    requisition_report=requisition_report,
                    map_area=map_area)
        else:
            context.update(requisition_report=self.requisition_report())
        context.update(requisition_report_form=requisition_report_form)
        return context
