from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'accounts/login.html')


def home(request):
    return render(request, 'accounts/home.html')


def products(request):
    return render(request, 'accounts/Trainings.html')


def customer(request):
    return render(request, 'accounts/customer.html')
# Create your views here.
