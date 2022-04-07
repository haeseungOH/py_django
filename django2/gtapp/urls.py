# main urls.py 로 부터 위임받은 urls
from django.urls import path
from gtapp import views

urlpatterns = [
    path('insert', views.insertFunc),
    # path('insertok', views.insertokFunc),     
] 