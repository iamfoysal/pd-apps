from tkinter.tix import Form
from django import forms


class user_form(forms.Form):
       #<label for="user_name">Full Name</label>
        #<input type="text" name="user_name" value="" required>
    user_name =forms.CharField()
    user_email = forms.EmailField() 