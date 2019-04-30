from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :

    USER_GRADE_CHOICES = {
        ('Bronze','Bronze'),
        ('Silver','Silver'),
        ('Gold','Gold')
    }
    
    name= models.CharField(blank=True, max_length=255, default='')
    phone = models.CharField(max_length=40, null=True)
    address= models.CharField(max_length=200, null=True)
    check_notification = models.DateTimeField(auto_now_add=True)
    grade= models.CharField(max_length=30, choices=USER_GRADE_CHOICES, null=True) 
    is_recognized = models.CharField(max_length=40, default='in_progress')


class Cat(models.Model) :

    name = models.CharField(max_length=20, default='unknown')
    age = models.CharField(max_length =10, default='0')
    breed = models.CharField(max_length =10, default='unknown')
    image = models.ImageField(null=True, blank=True, upload_to = 'cat_image/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cats')
    birth = models.CharField(max_length=20,default='unknown')
    gender= models.CharField(max_length=10,default='unknown')
    eatinghabit= models.TextField(default='')
    health= models.TextField(default='')
    route=models.TextField(default='')
    meet=models.TextField(default='')
    neutral=models.CharField(max_length=10,default='unknown')
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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='create_notifications')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='receive_notifications')
    is_checked=models.BooleanField(default=False)
    


    def __str__(self) :
        return self.category + "-" + str(self.created_at)

class Article(models.Model) :

    ARTICLE_CATEGORY_CHOICES ={
        ('veterinary_medicine','veterinary_medicine'),
        ('nutrition','nutrition'),
        ('psychology','psychology')
    }

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='articles')
    title = models.CharField(max_length=100,default='')
    category= models.CharField(max_length=20, choices=ARTICLE_CATEGORY_CHOICES, default='veterinary_medicine')
    view=models.IntegerField(default=0)
    content=models.TextField()

    def __str__(self) :
        return self.title + " - " + str(self.creator.username)

    @property
    def like_count(self) :
        return self.likes.all().count()

    @property
    def comment_count(self) :
        return self.comments.all().count()

    class Meta :
        ordering = ['-created_at']


class ArticleImage(models.Model) :
    
    file = models.ImageField(upload_to = 'articleImage/')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='aricleImages'),

    def __str__(self) :
        return self.article.title

class Like(models.Model) :
  
    creator= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article= models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')

    def __str__(self) :
        return self.creator.username + " - " + self.article.title

class Comment(models.Model) :
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    content = models.CharField(max_length=300, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.creator.username +" - "+self.article.title+ " - "+self.content

    class Meta :
        ordering = ['created_at']


class ReComment(models.Model) :
    creator = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='recomments')
    content = models.CharField(max_length=300, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.creator.username + " - "+self.comment.article.title+ " - " + self.content
    
    class Meta :
        ordering = ['created_at']

class SummerNoteImage(models.Model) :

    file = models.ImageField(upload_to='summernoteImage/')
    url = models.TextField(default='', null=True, blank=True)