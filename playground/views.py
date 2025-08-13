from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from . import Sql
from .forms import StudentForm
from .model import Student


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

def forms(request):
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

def base(req):
    return render(req,"Base/Base.html")

def reg(request):
    error = "Password doesn't match"
    if request.method == "POST":

        
        name = request.POST.get("name")
        email = request.POST.get("email")
        passw = request.POST.get("password")
        conp = request.POST.get("conpassword")
        if passw == conp:
            Sql.insert_data(User(name,email,passw)) 
            return render(request,"output.html",{"name":name,"email":email})
        return render(request,"Reg.html",{"error":error})     
    return render(request,"Reg.html")



def form(request):
    title = "title"
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
            return render(request,"Form.html",{"form":form,"error":form.errors})
    form = StudentForm()
    return render(request,"Form.html",{'form':form})

def getdata(request):
    student = Student.objects.all()
    return render(request,"all_students.html",{"students":student})


def get_by_id(request,id):
    # student = Student.objects.get(pk=id)
    students = Student.objects.filter(name="Amina")
    return render(request,"student.html",{'student':students})