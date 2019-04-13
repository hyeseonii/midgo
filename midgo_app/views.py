from django.shortcuts import render
from .models import *
import datetime
from django.http import JsonResponse
# Create your views here.

def index(request):
    user= User.objects.get(username='hyeseonii')
    print(user.cats.all())
    
    return render(request,"./index.html")

def main(request):
    
        user=request.user

        if not user.is_anonymous :
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

        else :

                return render(request,"./main.html")


def check_notification(request) :

        print(request.user)

        user = request.user
        time_now = datetime.datetime.now()
        user.check_notification = time_now
        user.save()

        result= {'result' :'true'}

        return JsonResponse(result)

def join(request) :


        return render(request,"./join.html")


def check_join(request) :

        if request.method == 'POST' :

                owner_id=request.POST['owner_id']
                owner_password=request.POST['owner_password']
                owner_name = request.POST['owner_name']
                owner_phonenum = request.POST['owner_phonenum']
                owner_address = request.POST['owner_address']
                owner_email = request.POST['owner_email']

                new_user =User.objects.create(
                        username=owner_id,
                        password= owner_password,
                        address = owner_address,
                        phone = owner_phonenum,
                        name=owner_name,
                        email=owner_email, 
                )

                new_user.save()

                images=request.FILES.getlist("cat_img")

                # for idx in range(len(images)):
                #         new_cat= Cat.objects.create(
                #            image=Images(idx),
                #         )


                print(new_user)
                print(request.POST)
                print(request.FILES)

                return render(request,'./main.html')


