"""Apps"""

from django.apps import AppConfig


class FrontendConfig(AppConfig):
    """Config for frontend"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "frontend"
