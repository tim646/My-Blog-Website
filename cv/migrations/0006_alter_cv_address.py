# Generated by Django 4.0.4 on 2022-05-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_cv_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.TextField(max_length=200),
        ),
    ]
