# Generated by Django 3.1.5 on 2021-03-01 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_driver_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='profile_photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_photos'),
        ),
    ]
