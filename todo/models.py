from django.db import models

# Create your models here.


class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
