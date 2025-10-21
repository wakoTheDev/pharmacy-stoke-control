from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Medicine(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='medicines')
    manufacturer = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()
    image = models.ImageField(upload_to='medicine_images/', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
