from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"Name: {self.name} Password: {self.password}"
    