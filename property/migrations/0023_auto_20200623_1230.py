# Generated by Django 3.0.6 on 2020-06-23 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0015_auto_20200622_1121'),
        ('property', '0022_auto_20200623_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='inquiry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Inquiry'),
        ),
    ]
