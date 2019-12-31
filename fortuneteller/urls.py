from django.contrib import admin
from django.urls import path, include
from .import views
app_name = 'fortuneteller'

urlpatterns = [
    path('fortune', views.show_fortune),
    path('request',views.request_fortune)
   ]