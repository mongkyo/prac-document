from django.db import models

__all__ = (
    'CommonInfo',
    'Student',
)


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):
        verbose_name = '학생'
        verbose_name_plural = '학생 목록'
