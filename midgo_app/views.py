from django.shortcuts import render
from .models import *
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
# Create your views here.

def index(request):
    
        user=request.user

        if not user.is_anonymous :
                
                context= {'user': user, 'login': 'true'}

                return render(request,"./index.html", context)

        else :
                context ={ 'login': 'false'}

                return render(request,"./index.html", context)
                

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
                new_user.set_password(owner_password)
                new_user.save()

                images=request.FILES.getlist("cat_img")

                for idx,cat_image in enumerate(images) :
                        new_cat = Cat.objects.create(
                                image=cat_image,
                                name=request.POST.getlist('cat_name')[idx],
                                gender = request.POST['cat_gender' + str(idx+1)],
                                birth= request.POST.getlist('cat_birth')[idx],
                                breed= request.POST.getlist('cat_breed')[idx],
                                owner= new_user,
                                eatinghabit = request.POST.getlist('cat_eatinghabit'+ str(idx+1)),
                                health= request.POST.getlist('cat_health'+str(idx+1)),
                                route=request.POST.getlist('cat_route')[idx],
                                meet=request.POST.getlist('cat_meet')[idx],
                                neutral = request.POST['cat_neutral' + str(idx+1)],
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

def recognizeUserlist(request):

        users=User.objects.filter(is_recognized='in_progress')

        context ={'users':users}

        return render(request, "./recognizeUserlist.html",context)

def recognizeUser(request,user_id) :

        user= User.objects.get(username=user_id)

        user_cats= user.cats.all()

        print(user_cats)

        print(len(user_cats))

        cats_num = len(user_cats)

        cats = [None] * 3
        
        print(cats)

        for idx, cat in enumerate(user_cats) :
                cats[idx] = cat

        print(cats)         

        context={'user' : user, 'cat1': cats[0], 'cat2':cats[1], 'cat3':cats[2], 'cats_num': cats_num}

        return render(request, "./recognizeUser.html", context) 

from django.contrib.auth import authenticate, login
@csrf_exempt
def login_check(request) :

        if(request.method =='POST') :

                username = request.POST['user_id']
                password = request.POST['user_password']
                user = authenticate(request, username=username, password=password)

                if user is not None :
                        if user.is_recognized =='unrecognized' :
                                print("승인이 반려된 사용자입니다.")

                                result = {"result" : "unrecognized"}
                                return JsonResponse(result)

                        elif user.is_recognized == 'recognized' :
                                print("승인 완료된 사용자입니다.")
                                login(request, user)
                                print(request.user)

                                result ={"result":"recognized"}
                                return JsonResponse(result)

                        elif user.is_recognized == 'in_progress' :
                                print("심사 중인 사용자입니다.")

                                result={"result":"in_progress"}
                                return JsonResponse(result)
                else :

                        result = {"result" :"failed"}
                        return JsonResponse(result)