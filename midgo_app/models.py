from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :

    check_notification = models.DateTimeField(auto_now_add=True)

class Cat(models.Model) :

    name = models.CharField(max_length=20, default='unknown')
    age = models.CharField(max_length =10, default='0')
    breed = models.CharField(max_length =10, default='unknown')
    image = models.ImageField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cats')

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