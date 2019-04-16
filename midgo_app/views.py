from django.shortcuts import render
from .models import *
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    
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

                for idx,cat_image in enumerate(images) :
                        new_cat = Cat.objects.create(
                                image=cat_image,
                                name=request.POST.getlist('cat_name')[idx],
                                gender = request.POST['cat_gender' + str(idx+1)],
                                birth= request.POST.getlist('cat_birth')[idx],
                                breed= request.POST.getlist('cat_breed')[idx],
                                owner=request.user,
                                eatinghabit = request.POST['cat_eatinghabit'+ str(idx+1)],
                                health= request.POST['cat_health'+str(idx+1)],
                                route=request.POST.getlist('cat_route')[idx],
                                meet=request.POST.getlist('cat_meet')[idx],
                        )
                        new_cat.save()
                

                print(new_user)
                print(request.POST)
                print(request.FILES)

                return redirect('/main/')

@csrf_exempt
def join_check_id(request) :

        if request.method =='POST' :
                
                user_id = request.POST['user_id']

                try:
                        user = User.objects.get(username = user_id)
                        result = {"result":"failed"}
                except:
                        result = {"result":"success"}

                return JsonResponse(result)

def login_page(request):

        return render(request,"./login_page.html")