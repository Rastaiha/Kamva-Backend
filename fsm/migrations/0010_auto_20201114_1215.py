# Generated by Django 3.0.8 on 2020-11-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0007_playerworkshop_last_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfileanswer',
            name='answer_file',
            field=models.FileField(max_length=4000, upload_to='AnswerFile'),
        ),
    ]
