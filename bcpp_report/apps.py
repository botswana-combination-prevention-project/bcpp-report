from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'bcpp_report'
    verbose_name = 'Bcpp Report'
    base_template_name = 'edc_base/base.html'
    app_label = 'bcpp_report'
