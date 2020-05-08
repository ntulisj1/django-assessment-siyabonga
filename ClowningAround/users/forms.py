"""Clowning Around Forms."""

from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):  # noqa
    class Meta(forms.UserChangeForm.Meta):  # noqa
        model = User


class UserCreationForm(forms.UserCreationForm):  # noqa

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):  # noqa
        model = User

    def clean_username(self):  # noqa
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])
