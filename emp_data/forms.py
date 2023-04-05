from django import forms
from .models import Employee


class employee_data_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'date', 'check_in','check_out')
        template_name = 'edit.html' 
        
        