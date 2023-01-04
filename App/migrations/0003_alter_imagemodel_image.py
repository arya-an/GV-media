# Generated by Django 4.1.4 on 2023-01-04 15:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_imagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='static/images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
    ]