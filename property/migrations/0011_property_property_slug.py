# Generated by Django 3.0.6 on 2020-06-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_remove_property_property_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_slug',
            field=models.SlugField(default='some_slug', editable=False, max_length=255),
        ),
    ]