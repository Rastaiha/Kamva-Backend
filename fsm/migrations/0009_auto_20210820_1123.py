# Generated by Django 3.1 on 2021-08-20 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0008_auto_20210820_1042'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='invitation',
            unique_together={('invitee', 'team')},
        ),
    ]
