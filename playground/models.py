from django.db import models

# Create your models here.
class product(models.Model):

    #id =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    amount = models.IntegerField()
    price = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
