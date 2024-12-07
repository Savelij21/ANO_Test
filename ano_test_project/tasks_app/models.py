from django.db import models

# Create your models here.


class Status(models.Model):
    """
    Модель статусов для задачи
    """
    name = models.CharField(max_length=30, unique=True)
    filter_name = models.CharField(max_length=30, unique=True)


class Task(models.Model):
    """
    Модель задачи
    """
    name = models.CharField(max_length=30, unique=True)
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
