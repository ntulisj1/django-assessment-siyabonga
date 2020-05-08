"""Clowning Around User App Configs."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """Config for users apps."""

    name = "users"
    verbose_name = _("Users")
