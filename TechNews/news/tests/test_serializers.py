from django.test import TestCase
from ..models import (
    News,
    Tags,
    Resources
)
from ..serializers import (
    NewsSerializer,
    TagsSerializer,
    ResourceSerializer
)


class NewsSerializerTest(TestCase):
    def setUp(self):
        self.tag_data = [
            {'title': 'Test Tag 1'},
            {'title': 'Test Tag 2'}
        ]
        self.resource_data = [
            {'title': 'Test Resource 1'},
            {'title': 'Test Resource 2'}
        ]
        self.news_data = {
            'title': 'Test News',
            'text': 'This is test news',
            'tags': self.tag_data,
            'resources': self.resource_data,
        }
        self.serializer = NewsSerializer(data=self.news_data)


    def test_news_serializer(self):

        if not self.serializer.is_valid():
            print(f"This is error : {self.serializer.errors}")

        self.assertTrue(self.serializer.is_valid())
        news = self.serializer.save()

        self.assertEqual(news.title, 'Test News')
        self.assertEqual(news.text, 'This is test news')
        self.assertEqual(news.tags.count(), 2)
        self.assertEqual(news.resources.count(), 2)
        self.assertEqual(news.tags.first().title, 'Test Tag 1')
        self.assertEqual(news.resources.first().title, 'Test Resource 1')


class TagsSerializerTest(TestCase):
    def setUp(self):
        self.tag_data ={'title': 'Test TagSerializer 1'}
        self.serializer = TagsSerializer(data=self.tag_data)

    def test_tags_serializer(self):
        if not self.serializer.is_valid():
            print(f'This is error : {self.serializer.errors}')

        self.assertTrue(self.serializer.is_valid())
        tags = self.serializer.save()

        self.assertEqual(tags.title, 'Test TagSerializer 1')

class ResourceSerializerTest(TestCase):
    def setUp(self):
        self.resource_data = {'title': 'Test ResourceSerializer 1'}
        self.serializer = ResourceSerializer(data=self.resource_data)

    def test_tags_serializer(self):
        if not self.serializer.is_valid():
            print(f'This is error : {self.serializer.errors}')

        self.assertTrue(self.serializer.is_valid())
        tags = self.serializer.save()

        self.assertEqual(tags.title, 'Test ResourceSerializer 1')
