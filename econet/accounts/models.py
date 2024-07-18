from django.db import models

class User(models.Model):    # 사용자 정보 정의
    user_id_number = models.AutoField(unique=True, primary_key=True)   # 유저 id(숫자)
    nickname = models.CharField(max_length=20, unique=True, error_messages={'unique': '이미 사용중인 별명입니다'})    # 유저 닉네임
    introduction = models.TextField(max_length=150, blank=True) # 유저 소개말
    joined_groups = models.ManyToManyField('Group', related_name='members', blank=True) # User 모델과 Group 모델 간의 다대다 관계 정의
    password = models.CharField(max_length=20)
    signup_date = models.DateTimeField(auto_now_add=True)   # 계정 생성 일자
    tier_choices = [
    #   ('DB 제공 값', '사용자 제공 값')
        ('tier1', 'Bronze'),
        ('tier2', 'Silver'),
        ('tier3', 'Gold'),
        ('tier4', 'Diamond'),
    ]
    tier = models.CharField(max_length=10, choices=tier_choices)
    consecutive_attendance_days = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # 연속 출석 일수 자동 업데이트
        if self.pk:  # 기존 사용자라면
            previous_instance = User.objects.get(pk=self.pk)
            if previous_instance.consecutive_attendance_days > 0:
                if self.signup_date == previous_instance.signup_date:
                    self.consecutive_attendance_days = previous_instance.consecutive_attendance_days + 1
                else:
                    self.consecutive_attendance_days = 1
            else:
                self.consecutive_attendance_days = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)  # 모임 id
    board_id = models.CharField(max_length=50)  # 게시판 id
    name = models.CharField(max_length=30)  # 모임 이름
    introduction = models.TextField(max_length=300)  # 모임 소개글
    members_count = models.IntegerField(default=0)  # 유저 수
    chat_link = models.URLField(blank=True)  # 모임톡방 링크
    activity_scope = models.CharField(max_length=100, blank=True)  # 모임 활동 범위(?)
    recruitment = models.BooleanField(default=False)  # 모임 모집 여부

    def __str__(self):
        return self.name
    