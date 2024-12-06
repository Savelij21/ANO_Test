
import time
import random

from src.celery import app
from celery.utils.log import get_task_logger

from .models import Task


logger = get_task_logger(__name__)


@app.task
def handle_task(task_id: int) -> None:
    # 1. Получение задачи из очереди
    task: Task = Task.objects.get(id=task_id)
    # 2. Изменение статуса задачи на "В процессе работы"
    task.status_id = 2
    task.save()
    logger.info(f'Задача {task.id}#{task.name} принята в обработку')
    # 3. Эмуляция выполнения задачи (например, случайная задержка 5-10 секунд)
    time.sleep(random.randint(5, 10))
    # 4. d.	Изменение статуса задачи на "Завершено успешно" или "Ошибка" (с некоторой вероятностью - 70%)
    success_chance: float = random.random()
    if success_chance <= 0.7:
        task.status_id = 3  # success
        logger.info(f'Задача {task.id}#{task.name} завершена успешно')
    else:
        task.status_id = 4  # error
        logger.error(f'Задача {task.id}#{task.name} завершена с ошибкой')
    task.save()


