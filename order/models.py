from django.db import models
import uuid
from accounts.models import Account
from cart.models import CartItem
from store.models import Product
# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254,blank=True,null=True)
    f_name = models.CharField(max_length=150)
    l_name = models.CharField(max_length=150)
    phone = models.CharField( max_length=15)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150,blank=True,null=True)
    city = models.CharField(max_length=150)
    
    @property
    def full_name(self):
        return f'{self.f_name} {self.l_name}'
    @property
    def full_address(self):
        return f'{self.address1} {self.address2}'
    
    def __str__(self):
        return f'{self.user.email} {self.full_name}'

class OrderProduct(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    order_notes = models.CharField(max_length=350)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def sub_total(self):
        return self.product.price * self.quantity
    @property
    def total(self):
        total = 0
        items = CartItem.objects.filter(user=self.user)
        for item in items:
            total += item.sub_total
        return total

    def __str__(self) -> str:
        return f'{self.order.full_name} {self.product}'



