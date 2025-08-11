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

def form(request):
    title = "Application form"
    passw = "swathi@123"
    error = "Password doesn't match"
    if request.method == "POST":
        title = "Output"
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zi = request.POST.get("zip")
        if passw == password:
            return render(request,"output.html",{"title":title,"email":email,"password":password,"address":address,"address2":address2,"city":city,"state":state,"zip":zi})
        return render(request,"form.html",{"error":error})     
    return render(request,"form.html",{"title":title})