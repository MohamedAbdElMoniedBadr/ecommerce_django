from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):

    #id =
    seller = models.ForeignKey(User , on_delete=models.SET_NULL ,null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    amount = models.IntegerField()
    price = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated','-added']

    def __str__(self):
        return self.name
    
