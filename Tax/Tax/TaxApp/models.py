from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User

#Paper igst 12  cgst 6 sgst 6
def convert_to_dict(obj):
    return obj.__dict__


# Create your models here.


class Product(models.Model):
    CATEGORY = (
            ( '4802', 'Paper'),
            ( '4820', 'Register'),
            ('4820','Books'),
            ('4820','Folders'),
            ('3215','Ball pen'),
            ('4419','Table'),
            ('9609','Pencil'),
            ('4202','Wallets'),
            
            )
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    #hsn=models.CharField(max_length=30)
    email= models.CharField(max_length=40)
    category = models.CharField(max_length=20, choices=CATEGORY, default='Paper')
    
    def __str__(self):
        return self.product_name
    def to_dict(self):
            return convert_to_dict(self)

class Code(models.Model):
    code=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name 


class Result (models.Model):
    identity=models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    profit=models.IntegerField()
    tax1=models.FloatField(default=None)
    tax2=models.FloatField(default=None)
    tax3=models.FloatField(default=None)
    hsn=models.CharField(max_length=30)




class Taxation(models.Model):
    code=models.CharField(max_length=200)
    cgst=models.FloatField()
    sgst=models.FloatField()
    igst=models.FloatField()
    def __str__(self):
        return self.code

   


