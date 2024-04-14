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
    

    def __str__(self) -> str:
        return f'{self.product} {self.user}'
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    
