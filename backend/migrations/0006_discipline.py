# Generated by Django 4.2.6 on 2023-10-13 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('workload', models.IntegerField()),
                ('students', models.ManyToManyField(related_name='disciplines', to='backend.student')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.teacher')),
            ],
            options={
                'db_table': 'disciplines',
            },
        ),
    ]
