from django.contrib.admin import AdminSite


class BcppReportAdminSite(AdminSite):
    site_title = 'Bcpp Report'
    site_header = 'Bcpp Report'
    index_title = 'Bcpp Report'
    site_url = '/'


bcpp_report_admin = BcppReportAdminSite(name='bcpp_report_admin')
