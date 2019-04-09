from django.shortcuts import render
from .models import *
import datetime
# Create your views here.

def index(request):
    user= User.objects.get(username='hyeseonii')
    print(user.cats.all())
    
    return render(request,"./index.html")

def main(request):
    
    user=request.user
    time_now = datetime.datetime.now()

    notifications = Notification.objects.filter(created_at__range=[user.check_notification, time_now])
    notifications_count = len(notifications)
    is_important = False
    for notification in notifications :
        if notification.category == 'reply' :
            is_important = True
            break


    context = { 'notifications' : notifications, 'notifications_count' : notifications_count, 'is_important' : is_important }
    print(context)
    return render(request,"./main.html",context)




