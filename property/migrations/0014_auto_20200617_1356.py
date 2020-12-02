# Generated by Django 3.0.6 on 2020-06-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_delete_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_image1',
            field=models.FileField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_image2',
            field=models.FileField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_image3',
            field=models.FileField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_image4',
            field=models.FileField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
    ]