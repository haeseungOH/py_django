"""django13_vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myvote import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.mainFunc),
    path('gogo/',views.dispFunc, name='disp'),  # ~/gogo/
    path('gogo/<int:question_id>/', views.detailFunc, name='detail'),               # ~/gogo/2/
    path('gogo/<int:question_id>/vote/', views.voteFunc, name='vote'),              # ~/gogo/2/vote/
    path('gogo/<int:question_id>/results/', views.resultFunc, name='results'),     # ~/gogo/2/vote/results
    
]
