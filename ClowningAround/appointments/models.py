"""ClowningAround Appointments model."""
from emoji_picker.widgets import EmojiPickerTextInputAdmin
from django.contrib.auth.models import AbstractUser
from users.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Appointment(models.Model):
    """Appoiments Schema."""

    STATUS = (
        ("UPCOMING", "upcoming"),
        ("INCIPIENT", "incipient"),
        ("COMPLETED", "completed"),
        ("CANCELLED", "cancelled"),
    )
    RATING = (("CLOWN", "🤡"), ("HAPPY", "🥳"), ("CHILLED", " 🤠"), ("LOVING", " 😍"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(_("Appointment Name"), max_length=128)
    status = models.CharField(
        _("Appointment Status"), choices=STATUS, default=1, max_length=50
    )
    date = models.DateField(default=timezone.now)
    issues = models.TextField(blank=True, null=True)
    rating = models.CharField(choices=RATING, max_length=255)

    def __str__(self):  # noqa
        return self.user.name
