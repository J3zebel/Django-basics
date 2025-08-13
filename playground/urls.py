from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello_world,name='hello'),
    path('name/', views.my_name,name='name'),
    path('yourname/<str:name>', views.your_name,name='yourname'),
    path('add/<int:num1>/<int:num2>', views.add,name='add'),
    path('index',views.index,name='index'),
    path('about/<str:name>', views.about,name="about"),
    path('forms/',views.forms,name="forms"),
    path('base/',views.base,name="base"),
    path('reg/',views.reg,name="reg"),
    path('form/',views.form,name="form"),
    path('all/',views.getdata,name="alldata"),
    path("getid/<int:id>",views.get_by_id,name="getidby")
]