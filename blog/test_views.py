from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.http import Http404
from .views import PostDetailedView


class Test_Views(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='123456'
        )
        self.user2 = User.objects.create_user(
            username='test_user2',
            password='123456'
        )
        self.post = Post.objects.create(
            title="Post Title",
            slug='post-title',
            author_id=1,
            content='hello this is post',
            featured_image='placeholder',
            created_on=timezone.now(),
            revised_on=timezone.now())
        self.comment = Comment.objects.create(
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

    def test_if_liked_post_is_liked(self):
        post = Post.objects.get(id=1)
        user = User.objects.get(username='test_user2')
        self.client.login(username='test_user2', password='123456')  # Log in the user
        post.likes.add(user)
        post.save()
        response = self.client.get(reverse('post_detailed_view', args=[post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], post)
        self.assertEqual(response.context['slug'], post.slug)
        self.assertTrue(response.context['liked'])
        
    def test_create_comment_valid_data(self):
        factory = RequestFactory()
        post = Post.objects.get(id=1)
        user = User.objects.get(username='test_user2')
        request = factory.post(reverse('post_detailed_view', args=[post.slug]))
        request.user = user
        valid_comment_data = {'content': 'Test comment content'}

        if valid_comment_data:
            request.POST = request.POST.copy()
            request.POST.update(valid_comment_data)
            initial_comment_count = Comment.objects.filter(post=post).count()
            response = PostDetailedView.as_view()(request, slug=post.slug)
            self.assertEqual(response.status_code, 200)
            final_comment_count = Comment.objects.filter(post=post).count()
            self.assertEqual(final_comment_count, initial_comment_count + 1)

    def test_create_comment_invalid_data(self):
        factory = RequestFactory()
        post = Post.objects.get(id=1)
        user = User.objects.get(username='test_user2')
        request = factory.post(reverse('post_detailed_view', args=[post.slug]))
        request.user = user
        invalid_comment_data = {}
        if not invalid_comment_data:
            response = PostDetailedView.as_view()(request, slug=post.slug)
            self.assertEqual(response.status_code, 200)
            
    def test_create_post(self):
        client = Client()
        client.login(username='test_user', password='123456')
        post_data = {
            'title': 'Test Post',
            'slug': 'test-post',
            'content': 'This is a test post content.',
            'author': self.user.id
        }
        response = client.post(reverse('create_post'), data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Test Post').exists())