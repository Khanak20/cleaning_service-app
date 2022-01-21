from django import forms
from django.db.models import fields
from .models import *
from django.conf import settings

class BookForm(forms.ModelForm):
    # date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = items
        fields = ['Title', 'Description','image']

class registeration(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'

class login_form(forms.ModelForm):
    class Meta:
        model = login
        fields = ['Email','Password']