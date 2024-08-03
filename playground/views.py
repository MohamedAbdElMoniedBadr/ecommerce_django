from django.shortcuts import render , redirect 
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
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    return render(request , 'product_form.html',context)

def updateProduct(request , pk):
    someProduct = product.objects.get(id = pk)
    form = ProductForm(instance = someProduct)
    if request.method == 'POST' :
        form = ProductForm(request.POST, instance=someProduct)
        if form.is_valid() :
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request,'product_form.html',context)

def deleteProduct(request,pk):
    someProduct = product.objects.get(id = pk)
    if request.method == 'POST':
        someProduct.delete()
        return redirect('home')
    return render(request , 'delete.html',{'item':someProduct})