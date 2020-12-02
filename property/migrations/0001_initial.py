# Generated by Django 3.0.6 on 2020-06-10 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zipcode', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('rooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('plot_size', models.IntegerField()),
                ('property_image_main', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('property_image1', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('is_published', models.CharField(choices=[('0', 'Active'), ('1', 'Inactive')], max_length=2)),
                ('is_active', models.CharField(choices=[('0', 'Active'), ('1', 'Inactive')], max_length=2)),
                ('is_deleted', models.CharField(choices=[('0', 'Active'), ('1', 'Inactive')], max_length=2)),
                ('created_by', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('realtor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtors')),
            ],
        ),
    ]
