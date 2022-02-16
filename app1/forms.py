from django import forms
from django.core import validators
from app1 import models



"""
def even_or_not(value):
       if value%2 == 1:
              raise forms.ValidationError("Please inseart an even number!!")
    
class user_form(forms.Form): 
  
   #  name = forms.CharField(validators= [validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
   #  number_field = forms.IntegerField(validators = [even_or_not])
   user_email = forms.EmailField()
   user_vmail = forms.EmailField()




   def clean (self):
      all_cleaned_data = super().clean()
      user_email = all_cleaned_data ['user_email']
      user_vmail = all_cleaned_data ['user_vmail']
      
      if user_email != user_vmail:
         raise forms.ValidationError("Your Email Don't match")

"""

class AsgardForm(forms.ModelForm):
   class Meta:
      model = models.Asgard

      fields = "__all__"
      # exclude = ['first_name']
      # fields = ('first_name', 'last_name',)
      