# Generated by Django 4.1.1 on 2023-05-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPI', '0002_remove_employee_prediction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='time_of_eval',
            field=models.DateTimeField(auto_now=True, verbose_name='time of evaluation'),
        ),
    ]
