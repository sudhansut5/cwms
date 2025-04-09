# App/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Process, SubProcess

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'off'}))
    analyst_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Analyst name', 'autocomplete': 'off'}))
    analyst_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Analyst email', 'autocomplete': 'off'}))
    supervisor_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Supervisor name', 'autocomplete': 'off'}))
    supervisor_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Supervisor email', 'autocomplete': 'off'}))
    process = forms.ModelChoiceField(queryset=Process.objects.all(), widget=forms.Select(attrs={'placeholder': 'Select a Process'}))
    sub_process = forms.ModelChoiceField(queryset=SubProcess.objects.all(), widget=forms.Select(attrs={'placeholder': 'Select a Sub-Process'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'off'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'autocomplete': 'off'}))

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'analyst_name', 'analyst_email', 'supervisor_name', 'supervisor_email', 'process', 'sub_process', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['process'].widget.choices = [('', 'Select a Process')] + list(self.fields['process'].widget.choices)[1:]
        self.fields['sub_process'].widget.choices = [('', 'Select a Sub-Process')] + list(self.fields['sub_process'].widget.choices)[1:]

    def clean_analyst_email(self):
        analyst_email = self.cleaned_data.get('analyst_email')
        if not analyst_email.endswith('@ana.com'):
            raise forms.ValidationError(
                'Invalid email domain. Please use @ana.com for analyst email.')
        return analyst_email

    def clean_supervisor_email(self):
        supervisor_email = self.cleaned_data.get('supervisor_email')
        if not supervisor_email.endswith('@ana.com'):
            raise forms.ValidationError(
                'Invalid email domain. Please use @ana.com for supervisor email.')
        return supervisor_email


class CustomAuthenticationForm(AuthenticationForm):
    pass  # No additional modifications needed for AuthenticationForm

