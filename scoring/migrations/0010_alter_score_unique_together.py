# Generated by Django 4.1.3 on 2023-02-08 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0009_rename_answer_comment_deliverable_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set(),
        ),
    ]