# Generated by Django 3.0.6 on 2020-06-10 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='realtor_id',
            new_name='realtor',
        ),
    ]
