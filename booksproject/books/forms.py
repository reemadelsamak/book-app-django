from dataclasses import fields
from django import forms
from .models import Book

class Book_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields= ['ISBN','title','description','publish_date','author','price','appropriate','poster']