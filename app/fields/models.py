from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField('이름', max_length=60)
    shirt_size = models.CharField(
        '셔츠 사이즈',
        max_length=1,
        choices=SHIRT_SIZES,
        help_text='S,M,L 중에 선택'
    )

    age = models.IntegerField(
        '나이',
        null=True,
        blank=True
    )
    stars = models.IntegerField('좋아요', default=0)
    nickname = models.CharField(
        '닉네임',
        max_length=50,
        null=True,
        blank=True,
        unique=True,
    )