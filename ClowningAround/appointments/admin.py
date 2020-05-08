from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):  # noqa
    list_display = ["user", "name", "status", "date", "rating"]


admin.site.register(Appointment, AppointmentAdmin)
