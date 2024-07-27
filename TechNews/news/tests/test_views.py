# test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import News, Tags, Resources

class NewsViewTest(APITestCase):
    def setUp(self):
        self.tag = Tags.objects.create(title='Test Tag')
        self.resource = Resources.objects.create(title='Test Resource')
        self.news_data = {
            'title': 'Test News 1',
            'text': 'This is a test news 1.',
            'tags': [{'title': 'Test Tag'}],
            'resources': [{'title': 'Test Resource'}],
        }



    def test_get_news_list(self):
        news = News.objects.create(title='Test News 2', text='This is a test news 2.')
        news.tags.add(self.tag)
        news.resources.add(self.resource)
        response = self.client.get('/api/news/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test News 2')

    def test_create_news(self):
        response = self.client.post('/api/news/', self.news_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.get().title, 'Test News 1')

class TagsViewTest(APITestCase):
    def setUp(self):
        self.tag_data = {'title': 'Test Tag'}

    def test_get_tags_list(self):
        Tags.objects.create(title='Test Tag')
        response = self.client.get('/api/tags/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Tag')

    def test_create_tag(self):
        response = self.client.post('/api/tags/', self.tag_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tags.objects.count(), 1)
        self.assertEqual(Tags.objects.get().title, 'Test Tag')

class ResourcesViewTest(APITestCase):
    def setUp(self):
        self.resource_data = {'title': 'Test Resource'}

    def test_get_resources_list(self):
        Resources.objects.create(title='Test Resource')
        response = self.client.get('/api/resources/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Resource')

    def test_create_resource(self):
        response = self.client.post('/api/resources/', self.resource_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Resources.objects.count(), 1)
        self.assertEqual(Resources.objects.get().title, 'Test Resource')
