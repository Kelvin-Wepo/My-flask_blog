import unittest
from app.models import Blog, User, Subscriber,Comment
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_charles = User(username='norah', password='norah1', email='test@test.com')
        self.new_blog = Blog(id=1, title='Test', content='This is a test blog', user_id=self.user_norah.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.content, 'This is a test blog')
        self.assertEquals(self.new_blog.user_id, self.user_kwepo.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        get_blog = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)