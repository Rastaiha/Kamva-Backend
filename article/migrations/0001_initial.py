# Generated by Django 4.1.7 on 2023-06-20 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0003_alter_paper_creation_date_alter_paper_update_date_and_more'),
        ('accounts', '0014_alter_educationalinstitute_polymorphic_ctype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('paper_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.paper')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover_page', models.ImageField(blank=True, null=True, upload_to='workshop/')),
                ('is_draft', models.BooleanField(default=True)),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='new_articles', to='accounts.educationalinstitute')),
                ('tags', models.ManyToManyField(related_name='articles', to='article.tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.paper',),
        ),
    ]
