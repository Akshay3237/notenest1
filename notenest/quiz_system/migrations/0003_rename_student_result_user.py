# Generated by Django 3.2.24 on 2024-02-27 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_system', '0002_alter_question_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='student',
            new_name='user',
        ),
    ]
