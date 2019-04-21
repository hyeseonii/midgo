# Generated by Django 2.1.7 on 2019-04-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midgo_app', '0007_auto_20190421_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='category',
            field=models.CharField(choices=[('notice', 'Notice'), ('reply', 'Reply')], max_length=30, null=True),
        ),
    ]
