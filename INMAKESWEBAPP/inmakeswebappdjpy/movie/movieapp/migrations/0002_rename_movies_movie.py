# Generated by Django 3.2.16 on 2022-12-11 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='movies',
            new_name='movie',
        ),
    ]
