from django.db import models

from pgvector.django import VectorExtension, VectorField

# Create your models here.
class ProductData(models.Model):
    product_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=100, unique=True)

    product_price = models.DecimalField(max_digits=9, decimal_places=2) 
    product_currency = models.CharField(max_length=3) 
    product_url = models.URLField(max_length=500) 
    product_image = models.URLField(max_length=500,blank=True)

    product_category = models.CharField(max_length=20)
    product_brand = models.CharField(max_length=20, blank=True)
    product_description = models.TextField(blank=True)


    product_is_available = models.BooleanField(null=True)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)
    product_is_active = models.BooleanField(null=True, default=True)

    
    
class ProductEmbedding(models.Model):
    embedding_source_type = models.CharField(max_length=20)
    embedding_source_text = models.CharField(max_length=255)
    embedding_vector = VectorField(dimensions=384, null=True)
    product_source = models.ForeignKey(ProductData, on_delete=models.CASCADE)