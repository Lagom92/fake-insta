from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=100)
    # image = models.ImageField(blank=True)
    # django imagekit 검색으로 알수있음
    image = ProcessedImageField(
            upload_to = 'posts/images', # 저장위치
            processors = [ResizeToFill(600,600)],    # 크기지정
            format = 'JPEG',
            options = {'quality':90}
        )
    