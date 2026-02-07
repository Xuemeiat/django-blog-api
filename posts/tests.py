from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testing@gmail.com",
            password="yanshi05",
        )

        cls.post = Post.objects.create(
            author=cls.user, 
            title="A test title",
            body="This is body",
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A test title"),
        self.assertEqual(self.post.body, "This is body"),
        self.assertEqual(str(self.post), "A test title")
