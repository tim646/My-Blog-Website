# Generated by Django 4.0.4 on 2022-05-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_alter_cv_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cv',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
