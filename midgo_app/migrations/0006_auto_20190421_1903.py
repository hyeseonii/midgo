# Generated by Django 2.1.7 on 2019-04-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0005_auto_20190417_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cat_image/'),
        ),
    ]
