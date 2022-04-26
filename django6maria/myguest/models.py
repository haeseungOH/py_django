from django.db import models

# Create your models here.
class Guest(models.Model):
    # myno = models.AutoField(auto_created = True, primary_key=True)  # id 자동생성 방지
    title = models.CharField(max_length = 50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    class Meta:                     # 정렬하기
        #ordering=('title',)
        #ordering=('title','id')
        ordering=('-id',)
        
    