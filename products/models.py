from django.db import models
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    amount = models.IntegerField(blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

