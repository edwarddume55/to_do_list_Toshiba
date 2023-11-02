from django.db import models


class Task(models.Model):
    tittle=models.CharField(max_length=150)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)