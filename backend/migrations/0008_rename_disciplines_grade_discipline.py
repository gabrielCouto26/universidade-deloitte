# Generated by Django 4.2.6 on 2023-10-14 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_discipline_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='disciplines',
            new_name='discipline',
        ),
    ]