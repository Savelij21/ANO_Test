from django.test import TestCase
from rest_framework import status

from .utils import generate_task_name
from .models import Task, Status

# Create your tests here.


class TaskTest(TestCase):

    def test_task_creation(self):
        new_task_name = generate_task_name()
        new_task = Task.objects.create(
            name=new_task_name
        )
        self.assertEqual(new_task.name, new_task_name)
        self.assertEqual(new_task.status.filter_name, 'new')

    # === test API ===
    def test_list_tasks_api(self):
        """
        Тестирование получения списка задач
        """
        # Создаем несколько задач
        for _ in range(3):
            Task.objects.create(name=generate_task_name())

        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем количество задач в ответе
        self.assertEqual(len(response.data), 3)

    def test_list_tasks_with_status_filter_api(self):
        """
        Тестирование фильтрации задач по статусу
        """
        # Создаем задачи
        task_1 = Task.objects.create(name=generate_task_name())
        task_2 = Task.objects.create(name=generate_task_name())

        # Изменяем статусы задач
        task_1.status = Status.objects.get(filter_name='in_progress')
        task_2.status = Status.objects.get(filter_name='success')
        task_1.save()
        task_2.save()

        # Фильтрация по статусу
        # -- in_progress
        response = self.client.get('/api/tasks/', {'status': 'in_progress'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status']['filter_name'], 'in_progress')

        # -- success
        response = self.client.get('/api/tasks/', {'status': 'success'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status']['filter_name'], 'success')

    def test_retrieve_task_api(self):
        """
        Тестирование получения задачи по ID
        """
        new_task_name = generate_task_name()
        task = Task.objects.create(name=new_task_name)

        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['id'], task.id)
        self.assertEqual(response.data['name'], task.name)

