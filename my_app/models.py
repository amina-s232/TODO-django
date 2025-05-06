from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class TaskModel(models.Model):
    task_name=models.CharField(max_length=100)
    created_date= models.DateField(auto_now_add=True)
    due_date=models.DateField()
    description=models.TextField(null=True,blank=True)
    category =[
        ('work','work'),
        ('personal','personal'),
        ('urgent','urgent')
    ]
    task_catagory=models.CharField(max_length=100,choices=category)
    completed_status=models.BooleanField(default=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)  #one to many 
    def __str__(self):
        return self.task_name

class Otpmodel(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    otp =models.CharField(max_length=100)
    created_at= models.DateField(auto_now_add=True)