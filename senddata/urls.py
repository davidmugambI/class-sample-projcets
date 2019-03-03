from django.urls import path
from . import views

urlpatterns =[
    path('', views.insertdata, name='insertdata'),
    path('view/', views.viewdata, name='view'),
]