from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True, help_text="Fallback valid image URL if no file is uploaded")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
