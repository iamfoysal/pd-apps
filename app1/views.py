from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Asgard, Album 
from app1 import forms 


def home(request):
    asgard_list = Asgard.objects.order_by('first_name')
    diction = {'text_1':'This is a list Asgard means (Musician)', 'asgard':asgard_list}
    return render(request,'app1/home.html', context=diction)
    

def about(request):
    return render(request,'app1/about.html')

def form (request):
    new_form = forms.user_form()
    diction  = {'test_form':new_form, 'heading_1':"This is user Form created in Django library"}
    if request.method == 'POST':
        new_form =forms.user_form(request.POST)
        diction.update({'test_form':new_form})

        if new_form.is_valid():
            
            # diction.update({'name': new_form.cleaned_data['name']})
            # diction.update({'number_field': new_form.cleaned_data['number_field']})
            diction.update({'field': 'Field Match!!'})
            diction.update({'form_submited':"Yes"})
           
            
    return render (request, 'app1/form.html', context=diction) 
    