# Generated by Django 4.2.6 on 2023-10-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Coordinator')], default=1)),
            ],
            options={
                'db_table': 'user_types',
            },
        ),
    ]