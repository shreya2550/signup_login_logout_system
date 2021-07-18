"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    #path('abc', views.abc, name='abc'),


    #including urls of main
    path('home2',views.home2,name='home2'),
   path('add-beneficiary',views.addBeneficiary,name='add-beneficiary'),
   path('update-beneficiary/<int:id>',views.updateBeneficiary,name='update-beneficiary'),
   path('delete-beneficiary/<int:id>',views.deleteBeneficiary,name='delete-beneficiary'),
   path('send-email/<int:id>',views.sendEmail,name='send-email'),

]
