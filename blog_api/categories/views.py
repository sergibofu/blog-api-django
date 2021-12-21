from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categories.models import Category
from categories.serializers import CategorySerializer
# Create your views here.
class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()

        categoriesSerializer = CategorySerializer(categories, many=True)

        return Response({'message': 'O.K', 'categories': categoriesSerializer.data })

    def post(self, request):

        category = Category(category=request.data.get('category'))

        category.save()
        return Response({'message': 'O.K POST', 'data': request.data.get('category')})
        
       

class CategoriesViewDetail(APIView):
    http_method_names = ['get', 'put', 'delete']
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            categorySerializer = CategorySerializer(category, many=False) 
            return Response({'data': categorySerializer.data})

        except Category.DoesNotExist:
            return Response({'error': 'error retriving database'})

    def put(self, request, pk):
        try:
            
            category = Category.objects.get(pk=pk)
            param_cat = request.data.get('category')
            
            if isinstance(param_cat, str):
                category.category = param_cat
                category.save()
            
            categorySerializer = CategorySerializer(category, many=False) 
            return Response({'data': categorySerializer.data})

        except Category.DoesNotExist:
            return Response({'error': 'error retriving database'})
        return Response({'it works: ': 'yes'})

        
    def delete(self, request, pk):
        try:
            
            category = Category.objects.get(pk=pk)
            
            res = category.delete()
            return Response({'data': res})

        except Category.DoesNotExist:
            return Response({'error': 'error retriving database'})

