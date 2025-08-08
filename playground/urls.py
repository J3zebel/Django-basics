from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello_world,name='hello'),
    path('name', views.my_name,name='name'),
    path('yourname/<str:name>', views.your_name,name='yourname'),
    path('add/<int:num1>/<int:num2>', views.add,name='add'),
    path('index',views.index,name='index'),
    path('about/<str:name>', views.about,name="about")
]