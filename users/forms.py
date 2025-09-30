from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    mobile = forms.CharField(
        required=True,
        validators=[forms.RegexField(
            regex=r'^01[0-2,5][0-9]{8}$',
            error_messages={'invalid': 'Enter a valid Egyptian mobile number.'}
        ).validators[0]]
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']
        help_texts = {
            'password1': None  
        }
