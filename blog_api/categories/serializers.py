from django.db.models import fields
from rest_framework import serializers
from categories.models import Category, PostCategory

#serializers here
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'category',)
        model = Category

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'post', 'category',)
        model = PostCategory