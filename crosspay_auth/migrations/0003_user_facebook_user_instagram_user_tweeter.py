# Generated by Django 4.0.6 on 2022-09-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crosspay_auth', '0002_user_banner_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(default='....', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(default='....', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='tweeter',
            field=models.URLField(default='....', max_length=500),
        ),
    ]
