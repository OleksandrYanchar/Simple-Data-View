from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductsListView.as_view(), name="produsts"),
    path("<slug:slug>/", views.ProductsDetailView.as_view(), name="product-info"),
]
