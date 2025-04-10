from django.db import models

# Create your models here.

class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField()
    observation = models.TextField()