from django.urls import path
from authshopcart import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
   # path('activate/<udib64>/<token>/',views.activate.as_view(),name='activate'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate.as_view(),name='activate')
]