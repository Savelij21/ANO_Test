
from .views import TaskViewSet


from django.urls import path


urlpatterns = [

    path('tasks/', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create_task',
    }), name='tasks'),

    path('tasks/<int:pk>/', TaskViewSet.as_view({
        'get': 'retrieve'
    }), name='task'),
]