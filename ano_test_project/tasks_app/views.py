import logging
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from .utils import generate_task_name
from .tasks import handle_task


logger = logging.getLogger(__name__)


class TaskViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для CRUD операция над объектами модели Task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['post'])
    def create_task(self, request, *args, **kwargs):
        """
        Метод для создания новой задачи
        """
        # -- создание новой задачи в БД
        new_task = Task.objects.create(
            name=generate_task_name()
        )
        # -- отправка задачи в очередь
        handle_task.delay(new_task.id)
        logger.info(f'Задача {new_task.id}#{new_task.name} создана и добавлена в очередь на обработку')

        return Response(
            data=self.serializer_class(new_task).data,
            status=201
        )

    def list(self, request, *args, **kwargs):
        """
        Метод для получения списка всех задач (с возможностью фильтрации через query параметр status)
        """
        status_filter = request.query_params.get('status', None)
        if status_filter:
            self.queryset = self.queryset.filter(status=int(status_filter))

        return super().list(request, *args, **kwargs)

