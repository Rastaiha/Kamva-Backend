# Generated by Django 4.1.3 on 2024-05-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0117_rename_target_state_playerhistory_state_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerHistory',
            new_name='PlayerStateHistory',
        ),
    ]