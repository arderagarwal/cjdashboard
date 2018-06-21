from django import forms
from django.contrib.auth.models import User
from recruiter.models import Recruiter

from django import forms
from django.contrib.auth.models import User
from recruiter.models import Recruiter

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','first_name','last_name','password',)
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','id':"formGroupExampleInput2", 'placeholder':"Username"}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':"exampleInputEmail1" ,'aria-describedby':"emailHelp", 'placeholder':"example@example.com"}),
            'first_name': forms.TextInput(attrs={'class':'form-control','id':"formGroupExampleInput2", 'placeholder':"First name"}),
            'last_name': forms.TextInput(attrs={'class':'form-control','id':"formGroupExampleInput2", 'placeholder':"Last name"}),
             'password': forms.PasswordInput(attrs={'type':"password" ,'class': 'form-control', 'id':"exampleInputPassword1" ,'placeholder':"Password"}),

        }

class RecruiterForm(forms.ModelForm):
    class Meta():
        model = Recruiter
        fields = ('PhoneNo',)
        widgets = {
            'PhoneNo': forms.TextInput(attrs={'class':'form-control','id':"formGroupExampleInput" ,'placeholder':"Phone Number"}),
        }
