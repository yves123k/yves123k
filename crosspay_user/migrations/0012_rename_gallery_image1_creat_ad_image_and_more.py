# Generated by Django 4.0.6 on 2022-09-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosspay_user', '0011_alter_creat_ad_gallery_image2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creat_ad',
            old_name='gallery_image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image10',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image11',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image12',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image2',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image3',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image4',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image5',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image6',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image7',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image8',
        ),
        migrations.RemoveField(
            model_name='creat_ad',
            name='gallery_image9',
        ),
        migrations.AddField(
            model_name='creat_ad',
            name='Titre',
            field=models.CharField(default='ND', max_length=100),
        ),
    ]