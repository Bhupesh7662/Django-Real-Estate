# Generated by Django 3.0.6 on 2020-06-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20200619_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='plot_size',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='property',
            name='rooms',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='property',
            name='sqft',
            field=models.CharField(max_length=150),
        ),
    ]