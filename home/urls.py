from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    
    path('',views.index,name='index'),
    #path('addtask',views.addtask,name='addtask'),
    #path('list',views.todoList,name='todolist'),
    path('contact',views.contact,name='contact'),
    path('checkout',views.checkout,name="checkout"),
    path('handlerequest/', views.handlerequest, name="HandleRequest")    
]
                        