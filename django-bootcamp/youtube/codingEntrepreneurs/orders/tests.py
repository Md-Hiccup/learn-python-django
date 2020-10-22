from django.contrib.auth import get_user_model
from django.test import TestCase

# from .models import Order

User = get_user_model()

# Create your tests here.
class OrderTestCase(TestCase):

    def setUp(self):  # camelCase - Python's builtin unittest
        user_a = User(username='test', email='test@invalid.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = '1234'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    # def test_create_order(self):
    #     obj = Order.objects.create(user=self.user_a, product=product_a)
