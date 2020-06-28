from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@bham.ac.uk', password='top_secret')
        Post.objects.create(author=self.user, title="TestCase1", content="Content test 1")

    def test_post_creation(self):
        test1 = Post.objects.get(title="TestCase1")
        self.assertEqual(test1.status, 0)
        self.assertEqual(test1.content, 'Content test 1')
        self.assertEqual(test1.title, 'TestCase1')


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')
