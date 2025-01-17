# Generated by Django 4.1.6 on 2023-02-07 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('number_of_employees', models.IntegerField(blank=True, null=True, verbose_name='number of employees')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('tone_of_voice', models.FloatField(blank=True, null=True, verbose_name='tone of voice')),
                ('starting_script', models.FloatField(blank=True, null=True, verbose_name='starting script')),
                ('ending_script', models.FloatField(blank=True, null=True, verbose_name='ending script')),
                ('solution_time', models.FloatField(blank=True, null=True, verbose_name='solution time')),
                ('choice_of_words', models.FloatField(blank=True, null=True, verbose_name='choice of words')),
                ('monthly_rating', models.FloatField(blank=True, null=True, verbose_name='monthly rating')),
                ('prediction', models.FloatField(blank=True, null=True, verbose_name='prediction')),
                ('last_month_rating', models.FloatField(blank=True, null=True, verbose_name='last month')),
                ('department', models.ForeignKey(default='CC INBOUND', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='KPI.department')),
            ],
        ),
    ]
