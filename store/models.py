from django.db import models
import uuid

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
