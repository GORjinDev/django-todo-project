from django.contrib import admin
from django.urls import path, include
from .views import index_view

app_name = 'todo_list'

urlpatterns = [
    path("", index_view, name='index')
]
