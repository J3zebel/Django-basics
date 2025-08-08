from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def hello_world(request):
    # return HttpResponse("Hello world")
    return redirect(reverse('index'))

def my_name(request):
    return HttpResponse("Swathi")

def your_name(request,name):
    return HttpResponse(f"Welcome {name}")

def add(request,num1,num2):
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")

def index(request):
    return render(request,"index.html")

def about(request,name):
    title = "about page"
    s = "what's up"
    return render(request,"about.html",{"title":title,"s":s,"name":name})