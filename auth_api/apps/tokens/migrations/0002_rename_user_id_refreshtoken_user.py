# Generated by Django 4.1.3 on 2022-12-19 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refreshtoken',
            old_name='user_id',
            new_name='user',
        ),
    ]
