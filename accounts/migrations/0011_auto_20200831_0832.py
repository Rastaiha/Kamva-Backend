# Generated by Django 3.1 on 2020-08-31 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0004_teamhistory_edge'),
        ('accounts', '0010_auto_20200830_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='current_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='fsm.fsmstate'),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
