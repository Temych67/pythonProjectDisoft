from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/tasks/", include("task_app.api.urls", "task_api")),
    path("api/account/", include("account.api.urls", "account_api")),
]
