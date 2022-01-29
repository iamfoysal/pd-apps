from datetime import date
from django import forms



class user_form(forms.Form):
       #<label for="user_name">Full Name</label>
        #<input type="text" name="user_name" value="" required>
    user_name =forms.CharField( label="Full Name", widget=forms.TextInput(attrs={'placeholder':'Enter your full name', 'style':'width:300px'}))
    
    user_dob =forms.DateField(label="Date Of Birth", widget=forms.TextInput(attrs={'type':'date'}))
    
    user_email = forms.EmailField(label="User Email", widget=forms.TextInput(attrs={'placeholder':'Enter Your Email'})) 
    