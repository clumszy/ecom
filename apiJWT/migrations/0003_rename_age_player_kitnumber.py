# Generated by Django 4.1.5 on 2023-04-06 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiJWT', '0002_league_team_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='age',
            new_name='kitNumber',
        ),
    ]