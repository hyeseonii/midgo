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

                notifications = Notification.objects.filter(receiver=user)
                notifications_count = 0
                for notification in notifications :
                        if not notification.is_checked :
                                notifications_count +=1

                is_important = False
                for notification in notifications :
                        if notification.category == 'reply' and notification.is_checked == False:
                                is_important = True
                                break


                context = { 'notifications' : notifications, 'notifications_count' : notifications_count, 'is_important' : is_important, 'user': user, 'login': 'true'}
                print(context)
                return render(request,"./main.html",context)

        else :

                return render(request,"./main.html")


def check_notification(request,notification_id) :

        print(request.user)

        user = request.user
        # time_now = datetime.datetime.now()
        # user.check_notification = time_now
        # user.save()

        checked_notification =Notification.objects.get(id=notification_id)
        checked_notification.is_checked =True
        checked_notification.save()

        result= {'result' :'true'}

        return JsonResponse(result)

def delete_notification(request, notification_id):
        
        notification = Notification.objects.get(id=notification_id)
        notification.delete()

        result= {'result' :'true'}

        return JsonResponse(result)

def delete_all_notification(request) :

        user=request.user

        my_notifications= Notification.objects.filter(receiver = user)
        print(my_notifications)
        for my_notification in my_notifications :
                my_notification.delete()

        result ={"result":"true"}

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

from django.contrib.auth import logout
def logout_page(request) :
        
        logout(request)

        return redirect('/main/')

def recognize(request,user_id,user_grade) :
        recognized_user = User.objects.get(username=user_id)
        recognized_user.is_recognized = 'recognized'
        recognized_user.grade = user_grade
        recognized_user.save()

        recognized_cats= recognized_user.cats.all()

        for cat in recognized_cats :
                cat.is_recognized = 'recognized'
                cat.save()

        return redirect('/recognizeUserlist/')

def unrecognize(request,user_id) :
        recognized_user = User.objects.get(username=user_id)
        recognized_user.is_recognized = 'unrecognized'
        recognized_user.save()

        recognized_cats= recognized_user.cats.all()

        for cat in recognized_cats :
                cat.is_recognized = 'unrecognized'
                cat.save()

        return redirect('/recognizeUserlist/')


def model(request):

        return render(request, "./model.html")


from django.core.paginator import Paginator

def study(request,category,page_idx):

        user = request.user

        if category == 'all' :
                articles= Article.objects.all()
        else :
                articles= Article.objects.filter(category = category) 

        print(articles)

        paginator = Paginator(articles, 2)

        start_idx = (page_idx-1) // 10 * 10 + 1
        end_idx = (page_idx-1) // 10 * 10 + 10
        if end_idx >=paginator.num_pages :
                end_idx = paginator.num_pages
        print(paginator.count)
        print(paginator.num_pages)
        print(paginator.page(page_idx))
        page_range = range(start_idx, end_idx+1)
        print(page_range)

        p = paginator.page(page_idx)

        prev_page_idx = page_idx - 1
        next_page_idx = page_idx + 1 

        context = {
                        'user': user, 
                        'login' : 'true', 
                        'articles': p, 
                        'page_range' :page_range, 
                        'category':category, 
                        'prev_page_idx' : prev_page_idx, 
                        'next_page_idx' : next_page_idx, 
                        'page_idx':page_idx,
                        'num_pages':paginator.num_pages, 
                        'article_count' : len(articles)
                }

        return render(request, "./study.html", context)

        
def addboard(request) :

        return render(request, "./addboard.html")

@csrf_exempt
def summernote_uploadImage(request) :

        if request.method =='POST' :
                
                print(request.FILES.getlist("uploadFile")[0])

                new_summernoteImage = SummerNoteImage.objects.create(
                        file = request.FILES.getlist('uploadFile')[0],
                )
                new_summernoteImage.save()

                new_summernoteImage.url = new_summernoteImage.file.url
                new_summernoteImage.save()
                #result = {'url': url}
                result ={'url': new_summernoteImage.url}
                return JsonResponse(result)


from bs4 import BeautifulSoup

def writeboard(request) :

        if request.method == 'POST' :

                user = request.user
                title = request.POST['title']
                category = request.POST['category']
                content = request.POST['editordata']
                soup = BeautifulSoup(content, 'html.parser')

                print(user)
                print(title)
                print(category)
                print(content)
                print(soup.find_all('img'))

                new_article = Article.objects.create(
                        creator = user,
                        title = title,
                        category = category,
                        content = content,
                )
                new_article.save()


                for link in soup.find_all('img') :
                        print(link.get('src'))
                        summernoteImage = SummerNoteImage.objects.get(url =link.get('src'))
                        print(summernoteImage)
                        new_article_image = ArticleImage.objects.create(
                                file = summernoteImage.file,
                                article = new_article,
                        )
                        new_article_image.save()

                all_user = User.objects.all()
                for receive_user in all_user :
                        new_notification = Notification.objects.create(
                                creator= user,
                                receiver = receive_user,
                                category = 'notice',
                                content = title,
                                article = new_article,
                        )
                        new_notification.save()


        return redirect('/main/study/'+category+"/1/")


def readboard (request,board_id) :

        user = request.user

        article = Article.objects.get(id = board_id)
        article.view += 1
        article.save()

        try :
                like = Like.objects.get(
                        creator=user,
                        article=article,
                )
                context ={'article':article, 'is_liked' :'했어요'}
        except :
                context ={'article':article, 'is_liked' :'좋아요'}
       

        return render(request, './readboard.html',context)

def like_board(request, board_id) :

        user=request.user

        article = Article.objects.get(id=board_id)

        new_like = Like.objects.create(
                creator=user,
                article=article,
        )

        new_like.save()

        result ={"result" : "success"}

        return JsonResponse(result)


def unlike_board(request, board_id) :

        user = request.user

        article =Article.objects.get(id = board_id)

        like = Like.objects.get(creator = user, article= article)

        like.delete()

        result = {"result": "success"}

        return JsonResponse(result)




