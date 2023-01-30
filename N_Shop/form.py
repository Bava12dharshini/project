from django.forms import ModelForm
from N_Shop.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 

class Createorderform(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['status']

class Createproductform(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
