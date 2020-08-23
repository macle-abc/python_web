from django.test import TestCase
from django.test import Client

from .models import *
from .views import *


class UserInfoTestCase(TestCase):
    def setUp(self):
        UserInfo.objects.create(nickname='昵称',
                                password='testtest',
                                account='testtest',
                                id_number='1' * 18,
                                email="test@qq.com",
                                sex='m',
                                security_question='name',
                                answer='test')

    def test_userinfo_create(self):
        userInfo = UserInfo.objects.get(account='testtest')
        self.assertEqual(userInfo.account, '1')

    def test_userinfo_center(self):
        c = Client()
        response = c.get("/user/center")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.charset, 'utf-8')
        self.assertNotIn('isLogin', response.cookies)
