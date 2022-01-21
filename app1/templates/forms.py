from django import forms
from django.db import models
from django.db.models import fields
from app1.models import items, login

class proform(forms.ModelForm):
    class Meta:
        model = login
        fields = ['Email','Password']

    class Meta1:
        model = items
        fields = ['Title' , 'Description' , 'image']