from django import forms
from .models import Post
from .models import Userreg
class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=Userreg
        fields='__all__'
    
    def clean_username(self):
        name=self.cleaned_data.get('username')
        if " " in name:
            raise forms.ValidationError('username cannot contain white spaces')
        return name
    
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirmpass=cleaned_data.get('confirm_password')

        if password!=confirmpass:
            raise forms.ValidationError("password amd confirm password should be same")

        return cleaned_data
    
    
    