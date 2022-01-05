# Generated by Django 4.0.1 on 2022-01-05 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_patient_primary_care_physician'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('diagnosis', models.CharField(max_length=100)),
                ('scheduled', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='appointment_doctors',
            field=models.ManyToManyField(through='hospital.Appointment', to='hospital.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
    ]