from django.db import models

# Create your models here.

class Item(models.Model):
    categories = (('Mobile','Mobile'),('Laptop','Laptop'),('Headphone','Headphone'))
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=900)
    item_desc = models.CharField(max_length=9000)
    item_price = models.IntegerField(default='0')
    item_image = models.ImageField(upload_to='images',default='')
    item_category = models.CharField(max_length=50,choices=categories,default='')


    def __str__(self):
        return str(self.item_name)