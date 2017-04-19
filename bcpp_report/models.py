from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow


class ReportFile(BaseUuidModel):

    name = models.CharField(
        verbose_name='Name',
        max_length=250,
        null=True,)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    map_area = models.CharField(
        verbose_name='Map area',
        max_length=250,
        null=True,)

    def __str__(self):
        return '{0}, {1} {2}'.format(
            self.name,
            self.map_area,
            self.report_datetime)

    class Meta:
        app_label = 'bcpp_report'
        unique_together = ("name", 'map_area', 'report_datetime')
