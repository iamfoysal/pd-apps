from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    diction = {'text_1':'I am a text send from views.py'}
    return render(request,'app1/home.html', context=diction)
    

def about(request):
    return render(request,'app1/about.html')