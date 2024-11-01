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