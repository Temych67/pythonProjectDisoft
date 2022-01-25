from django.urls import path
from task_app.api.views import (
    api_detail_task_view,
    api_update_task_view,
    api_delete_task_view,
    api_create_task_view,
    ApiAllTasksView,
)

app_name = "task_app"

urlpatterns = [
    # post url
    path("task_view/<title>", api_detail_task_view, name="detail_task"),
    path("task_view/<title>/update", api_update_task_view, name="update"),
    path("task_view/<title>/delete", api_delete_task_view, name="delete"),
    path("task/create", api_create_task_view, name="create"),
    path("all_tasks", ApiAllTasksView.as_view(), name="detail_all_tasks"),
]
