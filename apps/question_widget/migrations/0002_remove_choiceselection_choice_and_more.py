# Generated by Django 4.1.3 on 2024-01-02 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_widget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choiceselection',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='choiceselection',
            name='multi_choice_answer',
        ),
        migrations.RemoveField(
            model_name='inviteeusernameanswer',
            name='answer_ptr',
        ),
        migrations.RemoveField(
            model_name='inviteeusernameanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='longanswer',
            name='answer_ptr',
        ),
        migrations.RemoveField(
            model_name='longanswer',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='answer_ptr',
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='shortanswer',
            name='answer_ptr',
        ),
        migrations.RemoveField(
            model_name='shortanswer',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='uploadfileanswer',
            name='answer_ptr',
        ),
        migrations.RemoveField(
            model_name='uploadfileanswer',
            name='problem',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='ChoiceSelection',
        ),
        migrations.DeleteModel(
            name='InviteeUsernameAnswer',
        ),
        migrations.DeleteModel(
            name='LongAnswer',
        ),
        migrations.DeleteModel(
            name='MultiChoiceAnswer',
        ),
        migrations.DeleteModel(
            name='ShortAnswer',
        ),
        migrations.DeleteModel(
            name='UploadFileAnswer',
        ),
    ]