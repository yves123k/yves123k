# Generated by Django 4.0.6 on 2022-09-20 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='creat_Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(default=0, max_length=100)),
                ('total_piece', models.CharField(default=0, max_length=100)),
                ('rooms', models.CharField(default=0, max_length=100)),
                ('bathrooms', models.CharField(default=0, max_length=100)),
                ('living_area', models.CharField(default=0, max_length=100)),
                ('total_area', models.CharField(default=0, max_length=100)),
                ('distance_neightbors', models.CharField(default=0, max_length=100)),
                ('price_per_meter', models.CharField(default=0, max_length=100)),
                ('property_type', models.CharField(default=0, max_length=100)),
                ('year_built', models.CharField(blank=True, max_length=10)),
                ('price_per_m', models.CharField(blank=True, max_length=10)),
                ('for_rent', models.BooleanField(default=False)),
                ('on_sale', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True, max_length=40)),
                ('more_info', models.TextField(blank=True, max_length=400)),
                ('outside', models.TextField(blank=True, max_length=400)),
                ('other_information', models.TextField(blank=True, max_length=400)),
                ('gallery_image1', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image2', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image3', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image4', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image5', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image6', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image7', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image8', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image9', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image10', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image11', models.ImageField(blank=True, upload_to='Images')),
                ('gallery_image12', models.ImageField(blank=True, upload_to='Images')),
                ('main_img', models.ImageField(blank=True, upload_to='Images')),
                ('main_titre', models.CharField(blank=True, max_length=60)),
                ('main_description', models.TextField(blank=True, max_length=60)),
                ('main_price', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accounced', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
