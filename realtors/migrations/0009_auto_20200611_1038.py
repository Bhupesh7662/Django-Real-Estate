# Generated by Django 3.0.6 on 2020-06-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0008_auto_20200610_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtors',
            name='realtor_image',
            field=models.FileField(upload_to='media/%Y/%m/%d'),
        ),
    ]
