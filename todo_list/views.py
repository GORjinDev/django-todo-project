from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index_view(request: HttpRequest) -> HttpRequest:
    return render(request, "todo_list/index.html")
