# Generated by Django 3.1.5 on 2021-02-04 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210204_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]