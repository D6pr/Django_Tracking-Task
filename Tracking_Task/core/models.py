from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    status = models.CharField(choices=STATUS_CHOICES, default="todo")

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    
    priority = models.CharField(choices=PRIORITY_CHOICES, default="medium")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title