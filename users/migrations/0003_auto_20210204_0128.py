# Generated by Django 3.1.5 on 2021-02-04 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210204_0127'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drivers',
            new_name='Driver',
        ),
    ]