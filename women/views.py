from django.shortcuts import render
from django.http import HttpResponse

from .models import Women


def home(request):
    context = {
        'posts': Women.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
       
    }
    return render(request, 'about.html', context)

def add_page(request):
    return HttpResponse('')

def login(request):
    return HttpResponse('')

def show_post(request, post_id):
    context = {

    }
    return render(request, 'post.html')