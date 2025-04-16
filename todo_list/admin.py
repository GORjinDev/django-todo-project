from django.contrib import admin
from .models import ToDoItem

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'done', 'id']
    list_display_links = ['title', 'done', 'id']