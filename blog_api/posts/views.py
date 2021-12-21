from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

#Posts model and serializer 
from posts.models import Post
from posts.serializers import PostSerializer

#Categories and PostCategory models and serializers
from categories.models import Category, PostCategory
from categories.serializers import CategorySerializer , PostCategorySerializer  




# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, pk):
        try:
            #Primero recuperamos nuestro modelo
            post = Post.objects.get(pk=pk)
            postSerializer = PostSerializer(post, many=False) 

            #Con la clave primaria de nuestro modelo, recuperamos todas las relaciiones post-categoria
            #asociadas a nuestro post
            listOfCategoriesPost = PostCategory.objects.filter(post_id = pk)
            listOfCategoriesPostSerializer = PostCategorySerializer(listOfCategoriesPost, many=True)

            listOfcategories = []
            for category in listOfCategoriesPostSerializer.data:
                listOfcategories.append(category['category'])
            
            
            #ahora recuperamos los nombres de nuestras categorias en la bbdd
            categories = Category.objects.filter(pk__in=listOfcategories)
            categoriesSerializer = CategorySerializer(categories, many=True)

            return Response({'post': postSerializer.data, 'categories': categoriesSerializer.data})

        except Category.DoesNotExist:
            return Response({'error': 'error retriving database'})
    