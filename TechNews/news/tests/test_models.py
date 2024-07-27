from unittest import TestCase
from ..models import (
    News,
    Tags,
    Resources
)


class TagsModelTest(TestCase):

    def setUp(self):
        self.tag = Tags.objects.create(title='Test Tag')

    def test_tag_creation(self):
        self.assertEqual(self.tag.title, 'Test Tag')


class ResourcesModelTest(TestCase):
    def setUp(self):
        self.resource = Resources.objects.create(title='Test Resource')

    def test_resource_creation(self):
        self.assertEqual(self.resource.title, 'Test Resource')


class NewsModelTest(TestCase):
    def setUp(self):
        self.tag = Tags.objects.create(title="Test Tag for News")
        self.resource = Resources.objects.create(title="Test Resource for News")
        self.news = News.objects.create(title='Test News', text='This is a test news.')
        self.news.tags.add(self.tag)
        self.news.resources.add(self.resource)

    def test_news_creation(self):
        self.assertEqual(self.news.title, 'Test News')
        self.assertEqual(self.news.text, 'This is a test news.')

    def test_news_tags(self):
        self.assertIn(self.tag, self.news.tags.all())

    def test_news_resources(self):
        self.assertIn(self.resource, self.news.resources.all())
