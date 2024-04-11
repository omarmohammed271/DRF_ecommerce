from typing import Any, Iterable
import uuid
from django.db import models
from django.utils.text import slugify
from accounts.models import Account
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=150)
    description = models.TextField()
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categoryies")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})

class Size(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True,null=True)
    price = models.FloatField()
    size = models.ManyToManyField(Size,blank=True,null=True)
    color = models.ManyToManyField(Color,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
    def number_of_rating(self):
        rating = Review.objects.filter(product=self)
        return len(rating)
    
    def avg(self):
        rating = Review.objects.filter(product=self)
        stars=0
        for x in rating:
            stars += x.rating
        if len(rating) > 0:
            return stars/len(rating)    
        return 0


def upload_image(instance,file_name:str):
    extension = file_name.split('.')
    return f'products/{instance.product}.{extension}'

class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='products/')

    def __str__(self) -> str:
        return f'Images of **{self.product.name}**'

class Review(models.Model):
    user= models.ForeignKey(Account, on_delete=models.CASCADE)    
    product= models.ForeignKey(Product, on_delete=models.CASCADE) 
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField()
    def clean(self) -> None:
        if self.rating > 5:
            raise ValidationError('Rating max is 5')
        if self.rating <1:
            raise ValidationError('Rating minmum is 1')
        return super(Review,self).clean()   
    

    def __str__(self) -> str:
        return f'Review Of {self.product}'
    
class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    discount_precentage = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def price_after(self):
        ratio = (self.discount_precentage)/100
        price_in_ratio = self.product.price * ratio
        final_price = self.product.price - price_in_ratio 
        return final_price
    
    def __str__(self) -> str:
        return f'Offer of {self.product.name}'
    

