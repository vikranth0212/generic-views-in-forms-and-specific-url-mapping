from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)

    #it is used to done a dynamic url mapping or cananical url mapping
    #cananical url mapping is a process of creating url suffixes dynamically,based on selected instance
    #instance means present running or working or presented object
    #ie present in self 
    def get_absolute_url(self):
        return reverse('schooldetail',kwargs={'pk':self.pk})
        #reverse is used to take the control flow to respected url name
        #in reverse we gave schooldetails samething we need to give in url
        #get_absolute_url is a magic method or special method aautomatically called,particularly object method

    def __str__(self):
        return self.sname

class Student(models.Model):
    studentname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sloc=models.CharField(max_length=100)
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')
    #whatever we r giving related name here same thing need to five in htmlpage for loop jinja tag

    def __str__(self):
        return self.studentname   

       