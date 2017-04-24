"""bcpp_reports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from .admin_site import bcpp_report_admin
from .views import HomeView, ReportsView, GenerateReportFiles

app_name = 'bcpp-report'

urlpatterns = [
    url(r'^edc/', include('edc_base.urls', 'edc-base')),
    url(r'^tz_detect/', include('tz_detect.urls')),
    url(r'^admin/', bcpp_report_admin.urls),
    url(r'^reports/', ReportsView.as_view(), name='reports_view_url'),
    url(r'^generate_files/', GenerateReportFiles.as_view(), name='generate_report_files_url'),
    url(r'^', HomeView.as_view(), name='home_url'),
]
