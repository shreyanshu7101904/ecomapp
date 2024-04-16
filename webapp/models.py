from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, help_text="Your Product Name")
    price = models.FloatField(help_text="Product Price")
    description = models.CharField(max_length=1028, help_text="Your product description")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"
        ordering = ["-created_at"]

        
    def __str__(self):
        return self.name