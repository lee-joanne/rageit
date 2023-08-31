from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse
from .forms import CommentForm


class Test_Views(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='test_user', password='123456')
        test_user2 = User.objects.create_user(
            username='test_user2', password='123456')
        test_post = Post.objects.create(
            title="Post Title",
            slug='post-title',
            author_id=1,
            content='hello this is post',
            featured_image='placeholder',
            created_on=timezone.now(),
            revised_on=timezone.now())
        test_comment = Comment.objects.create(
            post_id=1,
            author_id=2,
            content="hello this is comment",
            created_on=timezone.now())

    def test_get(self):
        post = Post.objects.get(id=1)
        user = User.objects.get(username='test_user2')
        post.likes.add(user)
        post.save()
        post.likes.filter(id=user.id).exists()
        response = self.client.get(reverse('post_detailed_view', args=[post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], post)
        self.assertEqual(response.context['slug'], post.slug)
        self.assertTrue(post.likes.filter(id=user.id).exists())
        self.assertFalse(response.context['is_revised'])
