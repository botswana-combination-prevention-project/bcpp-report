from django.conf.urls import url, include

from .admin_site import bcpp_report_admin
from .views import HomeView

app_name = 'bcpp_report'

urlpatterns = [
    url(r'^edc/', include('edc_base.urls', 'edc-base')),
    url(r'^tz_detect/', include('tz_detect.urls')),
    url(r'^admin/', bcpp_report_admin.urls),
    url(r'^', HomeView.as_view(), name='home_url'),
]
