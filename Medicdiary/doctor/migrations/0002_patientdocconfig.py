# Generated by Django 3.1 on 2020-11-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDocConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('access_code', models.IntegerField()),
            ],
        ),
    ]
