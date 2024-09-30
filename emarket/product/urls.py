from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.Get_all_products,name='products'),
    path('products/<str:pk>/',views.Get_by_id_product,name='get_by_id_product'),
]
