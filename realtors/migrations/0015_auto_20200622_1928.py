# Generated by Django 3.0.6 on 2020-06-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0014_realtors_realtor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtors',
            name='realtor_slug',
            field=models.SlugField(editable=False, max_length=1000),
        ),
    ]
