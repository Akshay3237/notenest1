# Generated by Django 3.2.24 on 2024-02-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('s', 'Student'), ('t', 'Teacher'), ('p', 'Parent')], max_length=1),
        ),
    ]
