from datetime import date
from xmlrpc.client import boolean
from django import forms



class user_form(forms.Form):
       # when use html tag like this <label for="user_name">Full Name</label>
       # when use html tag like this <input type="text" name="user_name" value="" required>
       
    user_name =forms.CharField( label="Full Name", required=False, widget=forms.TextInput(attrs={'placeholder':'Enter your full name', 'style':'padding:6px'}))
    
    user_dob =forms.DateField(label="Date Of Birth",required=False, widget=forms.TextInput(attrs={'type':'date','style':'padding:6px'}))
    user_phone =forms.IntegerField(label="User Phone", required=False,widget=forms.NumberInput(attrs={'placeholder':'+880**********','style':'padding:6px','type':'number'}))
    user_email = forms.EmailField(label="User Email", required=False,  widget=forms.TextInput(attrs={'placeholder':'Enter Your Email','style':'padding:6px'})) 
    address_field = forms.CharField(max_length=40, min_length=10)
    boolean_field = forms.BooleanField(required=False) 
    
   #  set_password = forms.PasswordInput() 