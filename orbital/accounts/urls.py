from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('products/', views.products),
    path('customer/', views.customer),
    path('home/', views.home)
]
