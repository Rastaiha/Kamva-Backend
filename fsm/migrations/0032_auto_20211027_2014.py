# Generated by Django 3.1 on 2021-10-27 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0031_auto_20211027_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='certificate_name_X',
        ),
        migrations.RemoveField(
            model_name='registrationform',
            name='certificate_name_Y',
        ),
        migrations.RemoveField(
            model_name='registrationform',
            name='certificate_template',
        ),
        migrations.CreateModel(
            name='CertificateTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_type', models.CharField(blank=True, max_length=50, null=True)),
                ('template', models.FileField(blank=True, null=True, upload_to='certificate_templates/')),
                ('name_X', models.IntegerField(blank=True, default=None, null=True)),
                ('name_Y', models.IntegerField(blank=True, default=None, null=True)),
                ('registration_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_templates', to='fsm.registrationform')),
            ],
        ),
    ]
