# Generated by Django 3.0.7 on 2020-06-13 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matches', '0003_match_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='date',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team2',
        ),
    ]
