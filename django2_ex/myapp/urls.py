# main urls.py 로 부터 위임받은 urls
from django.urls import path
from myapp import views

urlpatterns = [
    path('show', views.sendFunc),
        
] 