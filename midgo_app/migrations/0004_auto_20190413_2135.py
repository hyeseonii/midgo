# Generated by Django 2.1.7 on 2019-04-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0003_auto_20190413_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='birth',
            field=models.CharField(default='unknown', max_length=20),
        ),
        migrations.AddField(
            model_name='cat',
            name='eatinghabit',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='gender',
            field=models.CharField(default='unknown', max_length=10),
        ),
        migrations.AddField(
            model_name='cat',
            name='health',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='meet',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='route',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notification',
            name='category',
            field=models.CharField(choices=[('notice', 'Notice'), ('reply', 'Reply')], max_length=30, null=True),
        ),
    ]