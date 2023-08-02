from django.urls import path
from ormexamples import views

urlpatterns = [
    path('onetoone', views.oneToOne, name='oneToOne'),
    path('onetomany', views.oneToMany, name='oneToMany'),
    path('manytomany', views.manyToMany, name='manyToMany')
]