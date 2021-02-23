# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('email', 'username', 'password')


# class CustomUserChangeForm(UserChangeForm):

#     class Meta(UserChangeForm):
#         model = CustomUser
#         fields = ('email', 'username', 'password')


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
    
    