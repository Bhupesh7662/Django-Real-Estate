# Generated by Django 3.0.6 on 2020-06-25 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0030_auto_20200625_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_property',
            name='is_active',
        ),
    ]
