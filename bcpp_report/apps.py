import os
import sys

from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'bcpp_report'
    verbose_name = 'Bcpp Report Map'
    base_template_name = 'edc_base/base.html'
    app_label = 'bcpp_report'
    report_files_path = os.path.join(settings.MEDIA_ROOT, 'bcpp_report')
    #  Files
    plots_file_path = file = os.path.join(
        report_files_path, 'plots_report_file.csv')
    household_structures_file_path = os.path.join(
        report_files_path, 'household_structure_report_file.csv')
    members_file_path = os.path.join(
        report_files_path, 'members_report_file.csv')
    requisitions_file_path = os.path.join(
        report_files_path, 'requisitions_report_file.csv')

    # Files headers
    plot_hearder = [
        'confirmed', 'ess', 'enrolled',
        'accessible', 'status', 'access_attempts', 'map_area']
    household_strucuture_hearder = [
        'survey_schedule', 'enumerated', 'enumeration_attempts',
        'enrolled', 'eligible_members', 'refused_enumeration']
    members_hearder = [
        'survey_schedule', 'eligible_member', 'eligible_subject',
        'present_today', 'enrollment_loss_completed', 'undecided',
        'refused', 'absent', 'refused_htc', 'htc']
    requisition_header = [
        'requisition_datetime', 'is_drawn', 'received',
        'processed', 'packed', 'shipped', 'panel_name',
        'subject_visit', 'study_site_name', 'subject_visit_id']
    subject_visit_header = ['id', 'survey_schedule']

    def ready(self):
        sys.stdout.write('Loading {} ...\n'.format(self.verbose_name))
        sys.stdout.write(' Done loading {}.\n'.format(self.verbose_name))
        if not os.path.exists(self.report_files_path):
            os.makedirs(self.report_files_path)
