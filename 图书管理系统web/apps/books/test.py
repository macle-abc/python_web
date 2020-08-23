from django.test import TestCase
from .models import *

class BookInfoTestCase(TestCase):
    # 测试用例执行前的操作

    def setUp(self):
        BookInfo.objects.create(number_of_existing=20, author='test', introduction="introduction", name="bookname",
                                ISBN='11111111111111111')

    def test_bookinfo_can_create(self):
        test = BookInfo.objects.get(ISBN='11111111111111111')
        self.assertEqual(test.number_of_existing, 20)
        self.assertEqual(test.author, 'test')
        self.assertEqual(test.introduction, 'introduction')
        self.assertEqual(test.name, 'bookname')
        self.assertEqual(test.ISBN, '1'*17)
