# Generated by Django 3.0.6 on 2020-06-10 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20200610_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtors',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='realtors',
            name='updated_date',
        ),
    ]