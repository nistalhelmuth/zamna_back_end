# Generated by Django 2.2.1 on 2019-05-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0008_remove_playlist_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='user',
            new_name='user_id',
        ),
    ]
