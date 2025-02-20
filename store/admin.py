# admin.py
from django.contrib import admin
from .models import Category, Product, ProductImage,StartaProject,ProjectImage,Project

# Define an inline class for ProjectImage
class ProductImageInline(admin.TabularInline):  # You can use StackedInline for a different layout
    model = ProductImage
    extra = 1  # Number of empty forms to display in the admin

# Customize the Project admin
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline] 
    # Include the ProjectImage inline in the Project admin
class ProjectImageInline(admin.TabularInline):  # You can use StackedInline for a different layout
    model = ProjectImage
    extra = 1  # Number of empty forms to display in the admin

# Customize the Project admin
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline] 

# Register your models
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)  
admin.site.register(Project, ProjectAdmin) 
admin.site.register(StartaProject)# Use the custom ProjectAdmin
