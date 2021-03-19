# Generated by Django 3.0.8 on 2021-03-07 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0002_auto_20210307_1918'),
        ('accounts', '0002_auto_20210307_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_event_owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_participated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mentor',
            name='workshops',
            field=models.ManyToManyField(related_name='workshop_mentors', to='fsm.FSM'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EventOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.ManyToManyField(related_name='event_owners', to='fsm.Event')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]