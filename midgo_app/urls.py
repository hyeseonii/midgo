from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('main/',views.main),
    path('main/check_notification/', views.check_notification),
    path('join/', views.join),
    path('login_page/',views.login_page),
    path('join/check_join/', views.check_join ),
    path('join/join_check_id/', views.join_check_id),
    path('recognizeUser/', views.recognizeUser)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
