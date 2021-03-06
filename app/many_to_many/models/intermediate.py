from django.db import models

__all__ = (
    'Person',
    'Group',
    'Membership',
)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        related_name='group_set',
        related_query_name='group',
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    date_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=64)