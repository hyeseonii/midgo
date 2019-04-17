from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :
    
    name= models.CharField(blank=True, max_length=255, default='')
    phone = models.CharField(max_length=40, null=True)
    address= models.CharField(max_length=200, null=True)
    check_notification = models.DateTimeField(auto_now_add=True)
    is_recognized = models.CharField(max_length=40, default='in_progress')


class Cat(models.Model) :

    name = models.CharField(max_length=20, default='unknown')
    age = models.CharField(max_length =10, default='0')
    breed = models.CharField(max_length =10, default='unknown')
    image = models.ImageField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cats')
    birth = models.CharField(max_length=20,default='unknown')
    gender= models.CharField(max_length=10,default='unknown')
    eatinghabit= models.TextField(default='')
    health= models.TextField(default='')
    route=models.TextField(default='')
    meet=models.TextField(default='')
    is_recognized = models.CharField(max_length=40, default='in_progress')
    



    def __str__(self) :
        return self.owner.username + " - " + self.name

class Notification(models.Model) :

    CATEGORY_CHOICES = {
        ('reply', 'Reply'),
        ('notice', 'Notice')
    }

    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.CharField(max_length = 30, choices=CATEGORY_CHOICES, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')

    def __str__(self) :
        return self.category + "-" + str(self.created_at)