from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=20)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    

    def __str__(self):
        return self.name
    
class Register(models.Model):
    e_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)
    def __str__(self):
        return self.username






