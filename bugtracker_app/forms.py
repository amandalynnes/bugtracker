from .models import CustomUser
from django import forms
from django.utils.timezone import now


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')


class LoginForm(forms.ModelForm):

    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class TicketItemForm(forms.Form):
    new = 'NW'
    done = 'DN'
    in_prograss = 'IP'
    invalid = 'IN'
    ticket_status_choices = [
        (new,'New'),
        (done,'Done'),
        (in_prograss, 'In_Prograss'),
        (invalid,'Invalid'),
    ]
    title = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, max_length=350)
    ticket_status = forms.ChoiceField(
        choices=ticket_status_choices,
    )
    
    