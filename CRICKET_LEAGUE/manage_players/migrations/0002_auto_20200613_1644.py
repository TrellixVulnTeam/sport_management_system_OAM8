# Generated by Django 3.0.7 on 2020-06-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image_uri',
            field=models.ImageField(upload_to='images/profile_images'),
        ),
    ]
