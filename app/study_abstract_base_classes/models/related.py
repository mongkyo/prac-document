from django.db import models

__all__ = (
    'RelatedUser',
    'PhotoPost',
    'TextPost',
)


class RelatedUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        RelatedUser,
        on_delete = models.CASCADE,
        # 유저(RelatedUser)입장에서
        # 자신이 특정 Post의 'author'인 경우에 해당하는 모든 PostBase를 참조하는 역방향 매니저 이름
        related_name = '%(class)s_set',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    # author의 related_name
    #       photopost_set
    photo_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'


class TextPost(PostBase):
    text = models.TextField(blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'
