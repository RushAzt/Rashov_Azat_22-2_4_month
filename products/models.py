from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    icon = models.ImageField(null=True)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    amount = models.IntegerField(blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}_{self.product}'
