import pandas as pd

from django.apps import apps as django_apps

from bcpp_subject.models import SubjectRequisition, SubjectVisit

from ..models import ReportFile


def report_files():
    return [
        [
            obj.name.split('/')[-1],
            obj.report_datetime.strftime("%B %d, %Y %H:%M"),
            obj.map_area] for obj in ReportFile.objects.all()]


def dump(qs, headers, outfile_name):
    """
    Dump a Django queryset and spits out a CSV file.
    """
    if 'subject_visit_id' in headers:
        headers = [field for field in headers if field != 'survey_schedule']
    q = qs.values(*headers)
    df = pd.DataFrame.from_records(q)

    #  Data frame for subject requisition
    if qs:
        if qs[0].__class__ == SubjectRequisition:
            subject_visit_header = django_apps.get_app_config(
                'bcpp_report').subject_visit_header
            q = qs.values(*headers)
            df1 = pd.DataFrame.from_records(q)
            visit_ids = []
            for requisition in qs:
                visit_ids.append(requisition.subject_visit.id)
            subject_visit_qs = SubjectVisit.objects.filter(id__in=visit_ids)
            visit_q = subject_visit_qs.values(*subject_visit_header)
            df2 = pd.DataFrame.from_records(visit_q)

            df = df1.merge(df2, left_on='subject_visit_id', right_on='id')

    df.to_csv(outfile_name, encoding='utf-8')
