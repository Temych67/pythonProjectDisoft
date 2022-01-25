from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_location(instance, filename):
    file_path = "task_image/{author_username}/{title}-{filename}".format(
        author_username=str(instance.author.username),
        title=str(instance.title),
        filename=filename,
    )
    return file_path


class TasksBook(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    content = models.TextField(max_length=1000, null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    whom_entrusted = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="Users", null=True, blank=True
    )
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published"
    )
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=TasksBook)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
