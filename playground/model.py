from  django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"name : {self.name}"

