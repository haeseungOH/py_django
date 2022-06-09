from django.db import models

# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length=10)
    tel = models.CharField(max_length=30)
    addr = models.CharField(max_length=50)
    
    class Meta:
        ordering=('-id',)   # 디센딩
    
    def __str__(self):
        return self.mname   # id에 대한 값을 읽어와준다. (위키룩스, 롯데리아 ..)

class Product(models.Model):
    pname = models.CharField(max_length=10)
    price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete=models.CASCADE)