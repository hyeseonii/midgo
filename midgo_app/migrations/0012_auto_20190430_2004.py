# Generated by Django 2.1.7 on 2019-04-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0011_auto_20190430_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Gold', 'Gold'), ('Silver', 'Silver')], max_length=30, null=True),
        ),
    ]
