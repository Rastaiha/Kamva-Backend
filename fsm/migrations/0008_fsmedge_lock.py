# Generated by Django 3.0.8 on 2021-03-27 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0007_auto_20210327_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='fsmedge',
            name='lock',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]