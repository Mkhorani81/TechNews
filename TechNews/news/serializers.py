from rest_framework import serializers

from .models import (
    News,
    Tags,
    Resources
)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    resources = ResourceSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'tags', 'resources']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        resources_data = validated_data.pop('resources')

        news = News.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, created = Tags.objects.get_or_create(title=tag_data['title'])
            news.tags.add(tag)

        for resource_data in resources_data:
            new_resource, created = Resources.objects.get_or_create(title=resource_data['title'])
            news.resources.add(new_resource)

        return news
