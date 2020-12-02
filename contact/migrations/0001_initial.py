# Generated by Django 3.0.6 on 2020-06-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquiry_name', models.CharField(max_length=100)),
                ('inquiry_email', models.EmailField(max_length=254)),
                ('inquiry_phone_number', models.CharField(max_length=20)),
                ('inquiry_message', models.TextField()),
            ],
        ),
    ]