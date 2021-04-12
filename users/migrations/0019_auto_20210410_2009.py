# Generated by Django 3.2 on 2021-04-11 00:09

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_application_sponsor_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='point_change_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='driver',
            name='profile_photo',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=50, size=[1920, 1080], upload_to='profile_photos'),
        ),
    ]