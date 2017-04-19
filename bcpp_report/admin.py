from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminReadOnlyMixin, ModelAdminAuditFieldsMixin)

from .admin_site import bcpp_report_admin
from .models import ReportFile
from .forms import ReportFileForm


class ModelAdminMixin(ModelAdminFormInstructionsMixin,
                      ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin,
                      ModelAdminReadOnlyMixin,
                      admin.ModelAdmin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(ReportFile, site=bcpp_report_admin)
class ReportFileAdmin(ModelAdminMixin):

    form = ReportFileForm
    list_per_page = 10

    list_display = ('name', 'report_datetime', 'created', 'modified')

    list_filter = (
        'created',
        'modified',
        'name',
        'hostname_modified')

    search_fields = ('name',)
