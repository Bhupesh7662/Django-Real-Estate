# Generated by Django 3.0.6 on 2020-06-25 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0029_auto_20200625_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_property',
            old_name='bathrooms',
            new_name='bedrooms',
        ),
    ]
