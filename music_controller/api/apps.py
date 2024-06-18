"""Apps"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Api config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
