from django.db import models

# Create your models here.

class Category(models.Model):
    # Schema for the Category model
    category_name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        # __str__ to represent itself in the form of a string
        return self.category_name


class Task(models.Model):
    # Schema for the Task model
    task_name = models.CharField(max_length=50, unique=True)
    task_description = models.TextField()
    is_urgent = models.BooleanField(default=False)
    due_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        # __str__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(self.id, self.task_name, self.is_urgent)
