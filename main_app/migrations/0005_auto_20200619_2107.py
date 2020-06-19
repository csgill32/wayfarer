# Generated by Django 3.0.7 on 2020-06-19 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200619_0118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
