# Generated by Django 3.1.5 on 2021-01-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DT', '0002_auto_20210125_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='area',
            name='area_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='available_time',
            name='aid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='co_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medical_report',
            name='medical_report_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='prescription_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='specialization_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]