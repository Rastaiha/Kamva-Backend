# Generated by Django 3.0.8 on 2020-08-31 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fsmpage',
            name='init_whiteboard',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
