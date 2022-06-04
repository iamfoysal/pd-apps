from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Asgard, Album 
from app1 import forms 


def home(request):
    asgard_list = Asgard.objects.order_by('first_name')
    diction = {'text_1': 'This is a (Musician List)', 'asgard': asgard_list}
    return render(request, 'app1/home.html', context=diction)
    

def about(request):
    return render(request, 'app1/about.html')


def demo(request):
    return render(request, 'app1/demo.html')


def form(request):
    new_form = forms.AsgardForm()
  
    if request.method == 'POST': 
        new_form = forms.AsgardForm(request.POST) 

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)
    
    diction = {'test_form': new_form, 'heading_1': 'Add new Musician'}

    return render(request, 'app1/form.html', context=diction)