# Generated by Django 3.0.6 on 2020-06-11 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0009_auto_20200611_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtors',
            name='hire_date',
        ),
    ]