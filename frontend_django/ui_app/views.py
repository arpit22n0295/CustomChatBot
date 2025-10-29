from django.shortcuts import render

def index(request):
    return render(request, "ui_app/index.html")
