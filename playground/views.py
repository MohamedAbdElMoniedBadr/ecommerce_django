from django.shortcuts import render
from .models import product
from .forms import ProductForm
# Create your views here.
def say_hello(request):
    items = product.objects.all()
    context = {"itemss" : items}
    return render(request , "home.html" , context)
def not_allowed(request):
    items = product.objects.all()
    context = {"itemss" : items}
    return render(request , "home.html" , context)
def createProduct(request):
    form = ProductForm()
    if request.method == 'post':
        form = ProductForm(request.POST)
    context = {'form' : form}
    return render(request , 'product_form.html',context)