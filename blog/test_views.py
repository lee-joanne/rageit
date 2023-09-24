from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.http import Http404
from .views import PostDetailedView
from django.core.exceptions import PermissionDenied


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
        self.client.login(username='test_user2', password='123456')
        post.likes.add(user)
        post.save()
        response = self.client.get(reverse('post_detailed_view', args=[post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], post)
        self.assertEqual(response.context['slug'], post.slug)
        self.assertTrue(response.context['liked'])
        
    def test_create_comment_valid_data(self):
        post = Post.objects.get(id=1)
        user = User.objects.get(username='test_user2')
        valid_comment_data = {'content': 'Test comment content'}
        self.client.login(username='test_user2', password='123456')
        url = reverse('post_detailed_view', args=[post.slug])
        response = self.client.post(url, valid_comment_data, follow=True)
        self.assertEqual(response.status_code, 200)
        final_comment_count = Comment.objects.filter(post=post).count()
        self.assertEqual(final_comment_count, 2)

    def test_create_comment_invalid_data(self):
        post = Post.objects.get(id=1)
        user = User.objects.get(username='test_user2')
        invalid_comment_data = {}
        self.client.login(username='test_user2', password='123456')
        url = reverse('post_detailed_view', args=[post.slug])
        response = self.client.post(url, invalid_comment_data, follow=True)
        self.assertEqual(response.status_code, 200)
            
    def test_create_post(self):
        self.client.login(username='test_user', password='123456')
        post_data = {
            'title': 'Test Post',
            'slug': 'test-post',
            'content': 'This is a test post content.',
            'author': self.user.id
        }
        response = self.client.post(reverse('create_post'), data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Test Post').exists())
        
    def test_edit_post_access(self):
        self.client.login(username='test_user', password='123456')
        url = reverse('update_post', kwargs={'slug': 'post-title'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], self.post)

    def test_edit_post_permission_denied(self):
        post = Post.objects.get(id=1)
        self.client.login(username='test_user2', password='123456')
        url = reverse('update_post', args=[post.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
    def test_delete_view_permission_denied(self):
        post = Post.objects.get(id=1)
        self.client.login(username='test_user2', password='123456')
        url = reverse('delete_post', args=[post.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
    def test_delete_view_render_page(self):
        post = Post.objects.get(id=1)
        self.client.login(username='test_user', password='123456')
        url = reverse('delete_post', args=[post.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_delete_successful(self):
        self.client.login(username='test_user', password='123456')
        post = Post.objects.get(id=1)
        url = reverse('delete_post', args=[post.slug])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(slug='test-post').exists()) 