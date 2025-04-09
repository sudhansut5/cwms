# forms.py
from django import forms
from .models import Production,Quality_tracker
from django.utils import timezone
from datetime import datetime


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'

class DateRangeForm(forms.Form):
    date_received = forms.DateField(initial='02/15/2024')
    date_reviewed = forms.DateField(initial='02/26/2024')
    analyst_name = forms.ModelChoiceField(queryset=Production.objects.values_list('analyst_name', flat=True).distinct(), to_field_name='analyst_name', empty_label="Analyst Name", widget=forms.Select(attrs={'class': 'form-control my-select', 'style': 'height: 35px; width:250px; margin-top: 0px; margin-left: 6px; border: 1px solid #403E3E;'}))



class QualityForm(forms.ModelForm):
    class Meta:
        model = Quality_tracker
        fields = '__all__'
# ------------------randomizer code ---------------------------
def get_select_field_choices():
    # Define the choices for the select_field dynamically
    # Return a list of tuples, where each tuple contains a value and a display name
    return [
        ('Select Field', 'Select Field'),
        ('analyst_name', 'Analyst Name'),
        ('process', 'Process'),
        ('sub_process', 'Sub Process'),
        ('status','Status')
    ]
class RandomizerForm(forms.ModelForm):
    date_received = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_reviewed = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    percentage = forms.FloatField(min_value=1, max_value=100)
    select_field = forms.ChoiceField(widget=forms.Select(), choices=get_select_field_choices())
 
    class Meta:
        model = Production
        fields = ('date_received', 'date_reviewed', 'percentage', 'select_field')
 
    def clean(self):
        cleaned_data = super().clean()
        date_received = cleaned_data.get('date_received')
        date_reviewed = cleaned_data.get('date_reviewed')
        percentage = cleaned_data.get('percentage')
        if date_received and date_reviewed and percentage:
            if date_received > date_reviewed:
                self.add_error('date_received', 'Date received should be before date reviewed.')
            if percentage < 0 or percentage > 100:
                self.add_error('percentage', 'Percentage should be between 0 and 100.')
