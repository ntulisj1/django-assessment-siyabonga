from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):  # noqa
    def is_open_for_signup(self, request: HttpRequest):  # noqa
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):  # noqa
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):  # noqa
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
