# Generated by Django 3.1.5 on 2021-02-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_sponsor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='phone_num',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
    ]
