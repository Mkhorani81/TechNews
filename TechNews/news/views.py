from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    News,
    Tags,
    Resources
)
from .serializers import (
    NewsSerializer,
    TagsSerializer,
    ResourceSerializer
)


# Create your views here.

class NewsListCreateAPIView(APIView):
    def get(self, request):
        tag_ids = request.query_params.getlist('tags')

        if tag_ids:
            valid_tag_ids = Tags.objects.filter(id__in=tag_ids).values_list('id', flat=True)
            news = News.objects.filter(tags__id__in=valid_tag_ids).distinct()
        else:
            news = News.objects.all()

        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagsListCreateAPIView(APIView):
    def get(self, request):
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourcesListCreateAPIView(APIView):
    def get(self, request):
        resources = Resources.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
