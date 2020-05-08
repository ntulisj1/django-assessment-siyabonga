"""ClowningAround User model."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """User schema."""

    is_troupe_leader = models.BooleanField(default=False)
    is_clown = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):  # noqa
        return reverse("users:detail", kwargs={"username": self.username})


class Troupe(models.Model):
    """Trouple Schema."""

    name = models.CharField(max_length=128)
    max_capacity = models.IntegerField(default=1)

    def __str__(self):  # noqa
        return self.name


class TroupeLeader(models.Model):
    """Trouple Leader Schema."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    troupe = models.ForeignKey(Troupe, on_delete=models.PROTECT)

    def __str__(self):  # noqa
        return f"{self.user.name} leads {self.troupe}"


class Clown(models.Model):
    """Clown Schema."""

    CLOWN_RANKS = ((1, "Top Dan"), (2, "Some Bob"), (3, "Maybe Harry"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rank = models.IntegerField()
    troupe = models.ForeignKey(Troupe, on_delete=models.PROTECT)

    def __str__(self):  # noqa
        return f"{self.user.name} from {self.troupe.name}"


class Client(models.Model):
    """Client Schema."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact_name = models.CharField(_("Name"), max_length=128)
    contact_email = models.EmailField(_("Email"), unique=True)
    contact_number = models.CharField(_("Contact Number"), max_length=16)

    def __str__(self):  # noqa
        return self.user.name
