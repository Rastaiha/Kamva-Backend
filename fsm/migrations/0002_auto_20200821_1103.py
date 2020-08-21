# Generated by Django 3.0.8 on 2020-08-21 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='edge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='fsm.FSMEdge'),
        ),
        migrations.AlterField(
            model_name='biganswer',
            name='problem',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='fsm.ProblemBigAnswer'),
        ),
        migrations.AlterField(
            model_name='multichoiceanswer',
            name='problem',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='fsm.ProblemMultiChoice'),
        ),
        migrations.AlterField(
            model_name='smallanswer',
            name='problem',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='fsm.ProblemSmallAnswer'),
        ),
    ]
