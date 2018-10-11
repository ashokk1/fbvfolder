from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
@api_view('GET','POST')
def ProductList(request):
    if request.method=='GET':
        products=Product.objects.all()
        serializers=ProductSerializer(products,many=True)
        return Response(serializers.data)
    elif request.method=='POST':
        serializers=ProductSerializer(data=request.data)
