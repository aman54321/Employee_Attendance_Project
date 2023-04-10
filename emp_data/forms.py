from django import forms
from .models import Employee


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)



class employee_data_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_id', 'name', 'date', 'check_in','check_out')
        template_name = 'edit.html' 
        
        
