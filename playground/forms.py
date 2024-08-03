from .models import product 
from django.forms import ModelForm


class ProductForm(ModelForm) :
    class Meta:
        model = product
        fields = '__all__'
