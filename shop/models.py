from django.db import models

# Create your models here.

class Product(models.Model):
    categories = (('Mobile','Mobile'),('Laptop','Laptop'),('Headphone','Headphone'))
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=9000)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='images',default='')
    product_category = models.CharField(max_length=50,choices=categories,default='')

    def __str__(self):
        return str(self.product_name)