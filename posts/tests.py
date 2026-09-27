from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTests(TestCase):
    def test_slug_is_generated_from_title(self):
        post = Post.objects.create(title='Hello World', body='Some content')
        self.assertEqual(post.slug, 'hello-world')

    def test_duplicate_titles_get_unique_slugs(self):
        first = Post.objects.create(title='Hello World', body='First')
        second = Post.objects.create(title='Hello World', body='Second')
        self.assertNotEqual(first.slug, second.slug)


class PostViewTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='First Post', body='Some content here')

    def test_index_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Post')

    def test_post_detail_returns_200(self):
        response = self.client.get(reverse('post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Some content here')

    def test_missing_post_returns_404(self):
        response = self.client.get('/post/does-not-exist/')
        self.assertEqual(response.status_code, 404)
