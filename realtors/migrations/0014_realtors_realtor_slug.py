# Generated by Django 3.0.6 on 2020-06-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0013_remove_realtors_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtors',
            name='realtor_slug',
            field=models.SlugField(default='some_slug', editable=False, max_length=1000),
        ),
    ]
