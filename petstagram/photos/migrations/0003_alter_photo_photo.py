# Generated by Django 5.1.2 on 2024-10-22 06:03

import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', validators=[petstagram.photos.validators.ImageSizeValidator(5)]),
        ),
    ]
