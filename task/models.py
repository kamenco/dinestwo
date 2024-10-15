from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    due_date = models.DateField()
    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
