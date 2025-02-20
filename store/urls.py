from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'store'

urlpatterns = [
    path('',views.home, name="home"),
    path('product/', views.product, name='product'),
    
    path('product_list/<int:category_id>/', views.product_list, name='product_list'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
     path('services/', views.services, name='services'),
       path('about/', views.about, name='about'),
       path('work/', views.project, name='work'),
         path('contact/', views.contact, name='contact'),
        #  path('start /', views.start, name='start'),
         path('contactc/', views.contactc, name='contactc'),
    path('success/', views.success, name='success'),
    
]

