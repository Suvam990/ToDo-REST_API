from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('To Do','To Do'),('In Progress','In Progress'),('Done','Done')])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title