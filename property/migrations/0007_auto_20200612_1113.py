# Generated by Django 3.0.6 on 2020-06-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20200612_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_slug',
            field=models.SlugField(editable=False, max_length=255),
        ),
    ]
