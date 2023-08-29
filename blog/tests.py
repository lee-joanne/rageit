from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.utils import timezone

# Create your tests here.

class Test_Create_Post(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='test_user', password='123456')
        test_user2 = User.objects.create_user(
            username='test_user2', password='123456')
        test_post = Post.objects.create(title="Post Title", slug='post-title', author_id=1, content='hello this is post', featured_image='placeholder', created_on=timezone.now(),
            revised_on=timezone.now())
        test_post.likes.add(test_user2)
    
    
    def test_string_title(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        self.assertEqual(str(post), post.title)
        
        
    def test_number_of_likes_count(self):
        post = Post.objects.get(id=1)
        likes_count = post.number_of_likes()
        self.assertEqual(likes_count, 1)
