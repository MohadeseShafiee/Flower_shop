from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    #image = models.ImageField(upload_to='categories')
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='Product/')
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name