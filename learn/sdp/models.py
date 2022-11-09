from django.db import models

#Create your models here.
class movie(models.Model):
    business= models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    thadd= models.CharField(max_length=200)
    city= models.CharField(max_length=200)
    zip= models.CharField(max_length=200)
    price= models.CharField(max_length=200)
    yaddress= models.CharField(max_length=200)
    ycity= models.CharField(max_length=200)
    yzip= models.CharField(max_length=200)
    phnum= models.CharField(max_length=200)
    email= models.CharField(max_length=200)

class cat(models.Model):
    sname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    pph = models.CharField(max_length=200)
    capacity=models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def str(self):
        return ' Name : ' + self.name + ' - Event : ' + self.sname
class music(models.Model):
    conname=models.CharField(max_length=200)
    nameor=models.CharField(max_length=200)
    conadd=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    yaddress=models.CharField(max_length=200)
    ycity=models.CharField(max_length=200)
    yzip=models.CharField(max_length=200)
    phno=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

class marriage(models.Model):
    hall1=models.CharField(max_length=200)
    halladd1=models.CharField(max_length=200)
    city1=models.CharField(max_length=200)
    zip1=models.CharField(max_length=200)
    pricepe1=models.CharField(max_length=200)
    capacity1=models.CharField(max_length=200)
    phno1=models.CharField(max_length=200)
    email1=models.CharField(max_length=200)











