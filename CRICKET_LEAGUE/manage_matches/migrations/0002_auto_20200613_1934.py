# Generated by Django 3.0.7 on 2020-06-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.CharField(max_length=10),
        ),
    ]
