# Generated by Django 3.1 on 2020-11-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_remove_records_patient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='access_code',
            field=models.IntegerField(default=1),
        ),
    ]
