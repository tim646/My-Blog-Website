# Generated by Django 4.0.4 on 2022-05-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='summary',
        ),
        migrations.AlterField(
            model_name='cv',
            name='title',
            field=models.TextField(max_length=40),
        ),
    ]
