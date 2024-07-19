from django.db import models

class CollectionBin(models.Model):
    bin_id_number = models.AutoField(unique=True, primary_key=True) # 수거함의 고유번호
    user_location = models.CharField(max_length=100)  # 사용자의 위치정보
    photo = models.ImageField(upload_to='bins/<int:pk>')  # 수거함의 사진
    description = models.TextField()  # 수거함의 위치를 설명하는 소개말
    acceptable_items = models.TextField()  # 수거함의 수거 대상 품목
    unacceptable_items = models.TextField()  # 수거함의 수거 불가 품목

    def __str__(self):
        return f'{self.user_location}의 수거함 {self.bin_id_number}'
