# Generated by Django 3.0.6 on 2020-06-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0017_realtors_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtors',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]