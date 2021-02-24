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
    description = forms.CharField(max_length=150)
    # filed_by = forms.ChoiceField(widget=forms.ChoiceField)
    ticket_status = forms.ChoiceField(
        choices=ticket_status_choices,
    )
    # assigned_to = forms.CharField(widget=forms.ChoiceField)
    # completed_by = forms.CharField(widget=forms.ChoiceField)
    
    