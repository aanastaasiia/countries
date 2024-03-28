
from main import views
from django.contrib import admin
from django.urls import path
import sqlite3
import requests



iid = 1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('country', views.country)
]


