# Generated by Django 4.0.6 on 2022-09-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosspay_user', '0012_rename_gallery_image1_creat_ad_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creat_ad',
            name='image',
            field=models.ImageField(blank=True, upload_to='ad'),
        ),
    ]