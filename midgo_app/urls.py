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
    path('join/check_join/', views.check_join ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
