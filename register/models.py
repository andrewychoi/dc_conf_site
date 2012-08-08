from django.db import models
from django import forms
from django.contrib.localflavor.us import models as us_models

# Create your models here.

class Registrant(models.Model):
    name = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    
    street_addr1 = models.CharField(max_length = 200, verbose_name="Street Address Line 1")
    street_addr2 = models.CharField(max_length = 200, verbose_name="Street Address Line 2")
    city = models.CharField(max_length = 200)
    state = us_models.USStateField()
    zip = models.CharField(max_length = 12)
    
    phone = us_models.PhoneNumberField()
    
    email = models.EmailField()
    diet = models.CharField(max_length = 200, verbose_name="Dietary restrictions")
    
class RegistrantForm(forms.ModelForm):
    class Meta:
        model = Registrant
