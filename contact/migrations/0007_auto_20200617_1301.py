# Generated by Django 3.0.6 on 2020-06-17 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20200617_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inquiry',
            old_name='property',
            new_name='property_id',
        ),
    ]
