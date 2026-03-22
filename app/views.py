from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import *
from app.serializers import *


class ProdcutCRUD(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Product is Created'})
        return Response({'Failed':'Product is not Created'})

    def put(self, request):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'Product is Updated'})
        return Response({'Failed':'Product is not Updated'})
        
    def delete(self, request):
        pass

    