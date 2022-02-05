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
        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob =new_form.cleaned_data['user_dob']
            user_phone = new_form.cleaned_data['user_phone']
            user_email = new_form.cleaned_data['user_email']  
            boolean_field = new_form.cleaned_data['boolean_field']
            address_field= new_form.cleaned_data['address_field']
            # set_password = new_form.cleaned_data['set_password']
            
            
            # diction.update({'set_password': set_password})
            diction.update({'address_field':address_field})
            diction.update({'boolean_field':boolean_field})
            diction.update({'user_name':user_name})       
            diction.update({'user_dob':user_dob})
            diction.update({'user_phone':user_phone})
            diction.update({'user_email':user_email})
            diction.update({'form_submited':"Yes"})
            
    return render (request, 'app1/form.html', context=diction) 
    