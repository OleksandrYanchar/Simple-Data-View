from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product

class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "products.html"
    context_object_name = 'products'
    
class ProductsDetailView(DetailView):   
    model = Product
    slug_field = "slug"
    template_name = "product-detail.html"
