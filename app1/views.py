from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Asgard, Album 


def home(request):
    asgard_list = Asgard.objects.order_by('first_name')
    diction = {'text_1':'This is a list Asgard means (Musician)', 'asgard':asgard_list}
    return render(request,'app1/home.html', context=diction)
    

def about(request):
    return render(request,'app1/about.html')

def form (request):
    diction  = {}
    return render (request, 'app1/form.html', context=diction)
    