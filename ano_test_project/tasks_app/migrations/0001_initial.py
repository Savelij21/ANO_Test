# Generated by Django 5.1.4 on 2024-12-07 12:00

import django.db.models.deletion
from django.db import migrations, models


def add_default_status(apps, schema_editor):
    """
    Автоматическое добавление статусов при создании БД
    """
    status_model = apps.get_model('tasks_app', 'Status')
    statuses = [
        ('Новая задача', 'new'),
        ('В процессе', 'in_progress'),
        ('Завершено успешно', 'success'),
        ('Ошибка', 'error'),
    ]
    for status in statuses:
        status_model.objects.get_or_create(name=status[0], filter_name=status[1])


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('filter_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tasks_app.status')),
            ],
        ),

        migrations.RunPython(add_default_status)
    ]
