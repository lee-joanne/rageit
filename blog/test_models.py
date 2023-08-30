from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify


class Test_Models(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='test_user', password='123456')
        test_user2 = User.objects.create_user(
            username='test_user2', password='123456')
        test_post = Post.objects.create(
            title="Post Title",
            slug='post-title',
            author_id=2,
            content='hello this is post',
            featured_image='placeholder',
            created_on=timezone.now(),
            revised_on=timezone.now())
        test_post.likes.add(test_user2)
        test_comment = Comment.objects.create(
            post_id=1,
            author_id=2,
            content="hello this is comment",
            created_on=timezone.now())

    def test_string_title(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        self.assertEqual(str(post), post.title)

    def test_number_of_likes_count(self):
        post = Post.objects.get(id=1)
        likes_count = post.number_of_likes()
        self.assertEqual(likes_count, 1)

    def test_post_comment_count(self):
        post = Post.objects.get(id=1)
        post_comment_count = post.number_of_comments()
        self.assertEqual(post_comment_count, 1)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        expected_url = reverse(
            "post_detailed_view", kwargs={
                "slug": "post-title"})
        actual_url = post.get_absolute_url()
        self.assertEqual(actual_url, expected_url)

    def test_slug_slugify(self):
        post = Post(
            title="Test Post",
            content="This is a test post",
            author_id=2)
        post.save()
        retrieved_post = Post.objects.get(id=post.id)
        expected_slug = slugify(post.title)
        self.assertEqual(retrieved_post.slug, expected_slug)

    def test_string_comment(self):
        comment = Comment.objects.get(id=1)
        expected_string = f"Comment by {comment.author}"
        self.assertEqual(comment.__str__(), expected_string)