from django.conf.urls import url, include

from .admin_site import bcpp_report_admin
from .views import HomeView, ReportsView, GenerateReportFiles

app_name = 'bcpp_report'

urlpatterns = [
    url(r'^edc/', include('edc_base.urls', 'edc-base')),
    url(r'^tz_detect/', include('tz_detect.urls')),
    url(r'^admin/', bcpp_report_admin.urls),
    url(r'^reports/', ReportsView.as_view(), name='reports_view_url'),
    url(r'^generate_files/', GenerateReportFiles.as_view(),
        name='generate_report_files_url'),
    url(r'^', HomeView.as_view(), name='home_url'),
]
