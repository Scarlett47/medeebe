from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from rest_framework import status

class NewsListView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetailView(APIView):
    def get(self, request, id):
        try:
            news_item = News.objects.get(id=id)
        except News.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news_item)
        return Response(serializer.data)