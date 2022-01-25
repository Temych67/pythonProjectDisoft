from rest_framework import serializers

from task_app.models import TasksBook
from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "email", "username"]


class TaskBarSerializer(serializers.ModelSerializer):
    whom_entrusted = RegistrationSerializer(read_only=True, many=True)

    class Meta:
        model = TasksBook
        fields = [
            "id",
            "title",
            "content",
            "author",
            "date_published",
            "whom_entrusted",
        ]


class TaskCreatorBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksBook
        fields = ["title", "content", "whom_entrusted"]
