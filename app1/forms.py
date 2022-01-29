from django import forms


class user_form(forms.Form):
       #<label for="user_name">Full Name</label>
        #<input type="text" name="user_name" value="" required>
    user_name =forms.CharField(required=True, initial="Mohammad Foysal", label="Full Name")
    user_email = forms.EmailField(label="User Email") 