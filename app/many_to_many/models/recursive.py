from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friend = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        friends_list = self.friend.all()
        friends_list_str = ', '.join([friend.name for friend in friends_list])
        return f'{self.name} (친구: {friends_list_str})'

