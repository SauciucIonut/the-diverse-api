# Generated by Django 3.1.7 on 2021-02-24 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dogs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cats',
            new_name='CatImage',
        ),
        migrations.RenameModel(
            old_name='Dogs',
            new_name='DogImage',
        ),
    ]
