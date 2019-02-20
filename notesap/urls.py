from django.urls import path
from . import views

app_name = 'notesap'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id>/',views.update, name='update'),
	path('<int:id>/delete/', views.delete, name='delete'),
]