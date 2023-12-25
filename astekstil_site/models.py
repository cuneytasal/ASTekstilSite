from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Product(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    english_product_name = models.CharField(max_length=100)
    french_product_name = models.CharField(max_length=100)
    english_product_color = models.CharField(max_length=100)
    french_product_color = models.CharField(max_length=100)
    product_image = models.ImageField(null=False, blank=False)

class EnglishColor(models.Model):
    class Meta:
        verbose_name = 'EnglishColor'
        verbose_name_plural = 'EnlishColors'
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
class FrenchColor(models.Model):
    class Meta:
        verbose_name = 'FrenchColor'
        verbose_name_plural = 'FrenchColors'
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name