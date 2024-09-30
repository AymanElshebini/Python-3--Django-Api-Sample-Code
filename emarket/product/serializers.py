from rest_framework import serializers
from .models import Product

class Productserializer(serializers.ModelSerializer):
    #وصف للحقول التي تظهر في الاي بي اي 
    class Meta:
        model=Product
        fields="__all__" #يقوم بعرض جميع البيانات 
      #  fields=('name','price','brand') #تقوم بعرض قيم محددة فقط 