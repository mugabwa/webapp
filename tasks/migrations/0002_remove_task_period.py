# Generated by Django 3.2.6 on 2021-09-07 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='period',
        ),
    ]
