import random
import string


def generate_task_name() -> str:
    """
    Генерирует случайное имя задачи
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))


