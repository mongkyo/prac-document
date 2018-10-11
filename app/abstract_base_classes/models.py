from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        # ordering = ['name']

    def __str__(self):
        return self.name


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
