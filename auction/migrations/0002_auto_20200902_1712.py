# Generated by Django 3.0.8 on 2020-09-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onetimeauction',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='onetimeauction',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]