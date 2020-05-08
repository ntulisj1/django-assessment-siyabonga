# Generated by Django 3.0.6 on 2020-05-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20200507_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('UPCOMING', 'upcoming'), ('INCIPIENT', 'incipient'), ('COMPLETED', 'completed'), ('CANCELLED', 'cancelled')], default=1, max_length=50, verbose_name='Appointment Status'),
        ),
    ]
