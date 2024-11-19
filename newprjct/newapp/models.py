from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    usertype=models.CharField(max_length=50)

class Department(models.Model):
    Dep_Name=models.CharField(max_length=100)

class Teacher(models.Model):
    depid=models.ForeignKey(Department,on_delete=models.CASCADE)
    tid=models.ForeignKey(User,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Address=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)



class Student(models.Model):
    depid=models.ForeignKey(Department,on_delete=models.CASCADE)
    sid=models.ForeignKey(User,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Address=models.CharField(max_length=100)