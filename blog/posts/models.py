from django.db import models

# 처리할 데이터를 models.py에 정의

class Post(models.Model):
    title = models.CharField(max_length=200)                # models.CharField() : 짧은 문자열(제목)
    body = models.TextField()                               # models.TextField() : 긴 문자열(내용)
    img = models.ImageField(upload_to = 'posts/image')
    created_at = models.DateTimeField(auto_now_add = True)  # models.DateTimeField() : 날짜와 시간을 나타내는 데이터
    updated_at = models.DateTimeField(auto_now = True)

# 작성한 model을 DataBase에 적용하는 명령어 : python manage.py makemigrations
# model을 DataBase에 migrate : python manage.py migrate
# admin 계정 생성 : python manage.py createsuperuser
    def __str__(self):
        return self.title

    def summary(self):      # 본문의 내용을 100글자로 제한
        return self.body[:220]