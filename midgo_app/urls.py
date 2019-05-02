from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('main/',views.main),
    path('main/model/',views.model),
    path('main/study/<str:category>/<int:page_idx>/',views.study),

    path('main/study/board/addboard/', views.addboard),
    path('main/study/board/addboard/write/',views.writeboard),
    path('main/study/board/addboard/summernote_uploadImage/',views.summernote_uploadImage),
    path('main/study/board/readboard/<int:board_id>/',views.readboard),
    path('main/study/board/readboard/<int:board_id>/add_comment/',views.add_comment),
    path('main/study/board/readboard/<int:board_id>/add_recomment/',views.add_recomment),
    path('main/study/board/readboard/<int:board_id>/check_recomment/',views.check_recomment),

    

    path('main/study/board/like/<int:board_id>/',views.like_board),
    path('main/study/board/unlike/<int:board_id>/',views.unlike_board),

    path('check_notification/<int:notification_id>/', views.check_notification),
    path('delete_notification/<int:notification_id>/',views.delete_notification),
    path('delete_all_notification/',views.delete_all_notification),
    

    path('join/', views.join),
    path('join/check_join/', views.check_join ),
    path('join/join_check_id/', views.join_check_id),

    path('login_page/',views.login_page),
    path('login_check/', views.login_check),

    
    path('recognizeUserlist/', views.recognizeUserlist),
    path('recognizeUser/<str:user_id>/', views.recognizeUser),
    path('recognizeUser/<str:user_id>/recognize/<str:user_grade>/', views.recognize),
    path('recognizeUser/<str:user_id>/unrecognize/',views.unrecognize),

    path('logout_page/',views.logout_page),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
