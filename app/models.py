from django.db import models
# Create your models here.
class Product_Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_id = models.IntegerField()

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category_name = models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return self.product_name
