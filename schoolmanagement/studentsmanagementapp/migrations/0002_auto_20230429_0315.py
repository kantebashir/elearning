# Generated by Django 3.0.5 on 2023-04-29 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsmanagementapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='session',
            name='start_year',
        ),
        migrations.AddField(
            model_name='session',
            name='Session',
            field=models.CharField(choices=[('Day', 'Day'), ('Evening', 'Evening'), ('Weekend', 'Weekend')], default='Day', max_length=15),
        ),
    ]