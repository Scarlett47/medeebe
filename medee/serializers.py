# news/serializers.py

from rest_framework import serializers
from .models import News, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Include id and name for the Category

class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Include category details as a nested serializer
    image = serializers.SerializerMethodField()  # To return the full URL for the image

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'author', 'category', 'created_at', 'source', 'image', 'views']

    def get_image(self, obj):
        # If image is uploaded, return its full URL, else return None
        if obj.image:
            return obj.image.url
        return None
