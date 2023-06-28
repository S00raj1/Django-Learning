from django.forms import ModelForm
from .models import *




class BookForm(ModelForm):

    class Meta:
        model = Book_location
        fields = '__all__'
        exclude = ['name']