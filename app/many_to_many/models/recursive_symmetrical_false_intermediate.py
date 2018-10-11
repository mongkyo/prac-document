from django.db import models


class TwitterUser(models.Model):
    """
    특정 유저가 다른 유저를 (인스턴스 메서드)
        follow  (팔로우하기)
        block   (차단하기)

    중간 모델이 저장하는 정보
        from_user
            어떤 유저가 '만든' 관계인지
        to_user
            관계의 '대상'이 되는 유저
        relation_type
            follow 또는 block (팔로우 또는 차단)

    용어 정리
        자신을 follow하는 사람목록
            followers (팔로워 목록)
        자신이 다른사람을 follow한 사람 목록
            following (팔로우 목록)
        자신이 block하는 다른 사람 목
            block_list
        A가 B를 follow한 경우
            A는 B의 follower  (팔로워)
            B는 A의 following (팔로우)
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
    )

    def __str__(self):
        return self.name
    @property
    def followers(self):
        """
        :return: 나를 follow하는 다른 TwitterUser QuerySet
        """

    @property
    def following(self):
        """
        :return: 내가 follow하는 다른 TwitterUser QuerySet
        """


    @property
    def block_list(self):
        """

        return: 내가 block하는 다른 TwitterUser QuerySet
        """

    def follow(self, user):
        """
        user를 follow하는 Relation을 생성
            1. 이미 존재한다면 만들지 않는다
            2. user가 block_list에 속한다면 만들지 않는다
        :param user: TwitterUser
        :return: tuple(Relation instance
        """

    def block(self, user):
        """
        user를 block하는 Relation을 생성
            1. 이미 존재한다면 만들지 않는다
            2. user가 following에 속한다면 해제시키고 만든다
        :param user: TwitterUser
        :return: tuple(Relation instance
        """


    @property
    def follower_relations(self):
        """
        :return: 나를 follow하는 Relation QuerySet
        """


    @property
    def followee_relations(self):
        """
        :return: 내가 follow하는 Relation QuerySet
        """




class Relation(models.Model):
    CHOICE_RELATION_TYPE = (
        ('f', 'follow'),
        ('b', 'block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relation_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relation_by_to_user',
    )

    relation_type = models.CharField(
        choices=CHOICE_RELATION_TYPE,
        max_length=1,
    )

    created_at = models.DateTimeField(auto_now_add=True)
