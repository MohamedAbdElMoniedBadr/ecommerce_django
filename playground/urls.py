from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.say_hello , name = 'home'),
    path("still/",views.not_allowed ),
    path("create-form/",views.createProduct,name = "create-form"),
    path("update-form/<str:pk>/",views.updateProduct,name = "update-form"),
    path("delete-form/<str:pk>/",views.deleteProduct,name = "delete-form")
]