# Generated by Django 3.0.6 on 2020-06-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0016_realtors_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtors',
            name='username',
            field=models.CharField(default='some user', max_length=100),
        ),
    ]
