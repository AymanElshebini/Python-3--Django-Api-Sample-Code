from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import Productserializer
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.
#instalation  django filters (pip install django-filter)
@api_view(['GET'])
def Get_all_products(request):
    #products=Product.objects.all()
    fillerset=ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    count=fillerset.qs.count()
    resPage=2
    paginator=PageNumberPagination()
    paginator.page_size=resPage
    queryset=paginator.paginate_queryset(fillerset.qs,request)
   
    serializer=Productserializer(queryset,many=True) 
    return Response({"products":serializer.data,"per page":resPage,"count":count})

@api_view(['GET'])
def Get_by_id_product(request,pk):
     
     products=get_object_or_404(Product,id=pk)
     serializer=Productserializer(products,many=False) # تحويل البيانات جيسون 
     return Response({"products":serializer.data})
