from django.db import models

# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.name

    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='product')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    
    

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    is_feature = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.title}"
    
class Project(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')
    is_feature = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.project.title}"

    
    
class StartaProject(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=150)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.name