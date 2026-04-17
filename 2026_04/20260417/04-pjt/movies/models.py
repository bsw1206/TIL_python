from django.db import models




class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=50)
    
    # 심화 과제 추가 필드
    director_img_url = models.URLField(blank=True, null=True) # 프로필 사진 [cite: 184]
    director_info = models.TextField(blank=True, null=True)   # 감독 정보 [cite: 187]
    director_works = models.TextField(blank=True, null=True)  # 대표 작품 목록 [cite: 188]

    def __str__(self):
        return self.title