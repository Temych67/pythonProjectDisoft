from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from account.models import Account
from task_app.models import TasksBook
from task_app.api.serializers import TaskBarSerializer, TaskCreatorBarSerializer

from django.core.mail import EmailMessage
from django.conf import settings
import threading
from django.template.loader import render_to_string

SUCCESS = "success"
ERROR = "error"
DELETE_SUCCESS = "deleted"
UPDATE_SUCCESS = "updated"
CREATE_SUCCESS = "created"


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_email_notice(user, task, request):
    email_subject = "Hi. You have new task!"
    email_body = render_to_string(
        "main_app_templates/email_message.html",
        {
            "user": user,
            "title": task.get("title"),
            "content": task.get("content"),
            "author": request.user.username,
        },
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )

    EmailThread(email).start()


@api_view(
    [
        "GET",
    ]
)
@permission_classes((IsAuthenticated,))
def api_detail_task_view(request, title):
    try:
        task = TasksBook.objects.get(title=title)
    except TasksBook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskBarSerializer(task)
        return Response(serializer.data)


@api_view(
    [
        "PUT",
    ]
)
@permission_classes((IsAuthenticated,))
def api_update_task_view(request, title):
    try:
        task = TasksBook.objects.get(title=title)
    except TasksBook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if task.author != user:
        return Response({"response": "You don`t have permission to edit that."})

    if request.method == "PUT":
        serializer = TaskCreatorBarSerializer(task, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data[SUCCESS] = UPDATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(
    [
        "DELETE",
    ]
)
@permission_classes((IsAuthenticated,))
def api_delete_task_view(request, title):
    try:
        task = TasksBook.objects.get(title=title)
    except TasksBook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if task.author != user:
        return Response({"response": "You don`t have permission to delete that."})

    if request.method == "DELETE":
        operation = task.delete()
        data = {}
        if operation:
            data[SUCCESS] = DELETE_SUCCESS
        return Response(data=data)


@api_view(
    [
        "POST",
    ]
)
@permission_classes((IsAuthenticated,))
def api_create_task_view(request):
    account = request.user
    task = TasksBook(author=account)

    if request.method == "POST":
        serializer = TaskCreatorBarSerializer(task, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            if len(serializer.data.get("whom_entrusted")) != 0:
                for pk in serializer.data.get("whom_entrusted"):
                    send_email_notice(
                        Account.objects.get(id=pk), serializer.data, request
                    )
            data[SUCCESS] = CREATE_SUCCESS
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiAllTasksView(ListAPIView):
    serializer_class = TaskBarSerializer
    queryset = TasksBook.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    search_fields = ("title", "content", "author")
