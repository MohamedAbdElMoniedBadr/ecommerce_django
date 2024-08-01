from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotAllowed
# Create your views here.
def say_hello(request):
    return render(request , "home.html")
def not_allowed(request):
    return HttpResponse("<h1 style = 'color:red'>no tamola allow</h1>")