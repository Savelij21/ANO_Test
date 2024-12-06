from rest_framework import serializers
from .models import Task, Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Task
        fields = '__all__'

