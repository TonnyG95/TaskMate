from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.task + " | " + "Done: " + str(self.done) + " | " + " important: " + str(self.important)
