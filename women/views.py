from django.shortcuts import render
from django.http import HttpResponse

def category(request, catid):
    context = {
        'catid': catid
    }
    return render(request, 'main.html', context)

def archive(request, year):
    context = {
        'year': year
    }
    return render(request, 'arch.html', context)