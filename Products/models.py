from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class product(models.Model):
    pName = models.CharField(max_length=20)
    nameShop = models.CharField(max_length=20)
    shopContact = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    email = models.EmailField()
    pPrice = models.DecimalField(max_digits=5, decimal_places=2, default=9.99)
    users = models.ManyToManyField(User , null=True , blank=True)

class Meta:
    dp_table = "product"
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.pName} - {self.quantity}"
    



