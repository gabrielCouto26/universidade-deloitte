# Generated by Django 4.2.6 on 2023-10-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.ManyToManyField(to='backend.permission'),
        )
    ]
