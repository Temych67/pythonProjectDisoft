from django.contrib import admin
from task_app.models import TasksBook


class TaskBookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_published")
    filter_horizontal = ("whom_entrusted",)


admin.site.register(TasksBook, TaskBookAdmin)
