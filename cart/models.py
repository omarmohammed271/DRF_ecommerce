from django.db import models
from store.models import Product,ImageProduct
from accounts.models import Account
import uuid
# Create your models here.
class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=150,blank=True,null=True)
    color = models.CharField(max_length=150,blank=True,null=True)
    

    def __str__(self) -> str:
        return f'{self.product} {self.user}'
    
    def sub_total(self):
        return self.product.price * self.quantity
    @property
    def total(self):
        total = 0
        items = CartItem.objects.filter(user=self.user)
        for item in items:
            total += item.sub_total()
        return total
    
    
    
