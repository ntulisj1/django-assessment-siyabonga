# Generated by Django 3.0.6 on 2020-05-07 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=128, verbose_name='Appointment Name')),
                ('status', models.CharField(max_length=255, verbose_name='Appointment Status')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('issues', models.TextField(blank=True, null=True)),
            ],
        ),
    ]