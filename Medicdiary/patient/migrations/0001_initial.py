# Generated by Django 3.0.7 on 2020-11-05 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientVitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Height_in_Centimeters', models.CharField(max_length=100)),
                ('Weight_in_kilograms', models.CharField(max_length=100)),
                ('Allergies', models.TextField(max_length=30)),
                ('Smoker_or_not', models.CharField(max_length=30)),
                ('Chronic_conditions', models.CharField(max_length=30)),
                ('patientv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=500)),
                ('phone', models.CharField(max_length=40)),
                ('emergency_contact', models.CharField(max_length=40)),
                ('profession', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(default='patients_profile_pictures/defaultprofilepic.jpg', upload_to='patients_profile_pictures')),
                ('Aadhar_Number', models.IntegerField()),
                ('usertype', models.IntegerField(default=1)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LabReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=100)),
                ('report_date', models.DateField()),
                ('upload_date', models.DateField(auto_now=True)),
                ('labreportfile', models.FileField(upload_to='PatientLabReports')),
                ('patientl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
