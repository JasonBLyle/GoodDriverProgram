# Generated by Django 3.1.5 on 2021-04-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210410_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointhist',
            name='sponsor_company',
            field=models.CharField(default='', max_length=30),
        ),
    ]
