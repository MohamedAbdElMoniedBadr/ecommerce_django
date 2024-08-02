from django.shortcuts import render
from .models import product
# Create your views here.
def say_hello(request):
    items = product.objects.all()
    context = {"itemss" : items}
    return render(request , "home.html" , context)
def not_allowed(request):
    return HttpResponse("<h1 style = 'color:red'>no tamola allow</h1>")