from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email']
        labels={
            'first_name' : 'First Name',
            'last_name':'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class PassChange(PasswordChangeForm):
    old_password = forms.CharField(label=_('old password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label=_('new password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label=_('confirm password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']
        labels = {
            'title':'Title',
            'description':'Description'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }

from .models import User

class studentRegistration(forms.Form):
    name=forms.CharField( max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), max_length=70)


class EditUserProfileForm(UserChangeForm):
    password= None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels= {'email': 'Email'}
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            # 'date_joined' : forms.DateInput(attrs={'class':'form-control'}),
            # 'last_login' : forms.DateInput(attrs={'class':'form-control'}),

        }


class EditAdminProfileForm(UserChangeForm):
    password= None
    class Meta:
        model = User
        # fields = ['username','first_name','last_name','email','date_joined','last_login']
        fields = '__all__'
        labels= {'email': 'Email'}
