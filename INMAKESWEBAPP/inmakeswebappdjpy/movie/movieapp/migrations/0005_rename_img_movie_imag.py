# Generated by Django 3.2.16 on 2022-12-11 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_alter_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='imag',
        ),
    ]
