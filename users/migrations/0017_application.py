# Generated by Django 3.1.5 on 2021-04-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210310_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(max_length=30)),
                ('sponsor', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]