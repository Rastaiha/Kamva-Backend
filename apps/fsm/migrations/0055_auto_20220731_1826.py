# Generated by Django 3.1 on 2022-07-31 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0054_auto_20220712_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aparat',
            old_name='id_link',
            new_name='video_id',
        ),
    ]