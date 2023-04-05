import django_filters

from .models import Employee

class DateFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = [
            'date',
            'name'
        ]