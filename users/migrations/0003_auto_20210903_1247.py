# Generated by Django 3.2.6 on 2021-09-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='newuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
