from django.db import models

from apps.books.models import *


class UserInfo(models.Model):
    nickname = models.CharField(verbose_name="昵称", max_length=20, help_text="最长不超过20个字符")
    avatar = models.ImageField(verbose_name="头像", null=True, blank=True, upload_to="user_avatar/%Y/%m/%d")
    password = models.CharField(verbose_name="密码", max_length=32, help_text="6-12个字符", db_index=True)
    account = models.CharField(verbose_name="账号", max_length=13, help_text="最长不超过13个字符", db_index=True,
                               primary_key=True)
    id_number = models.CharField(verbose_name="身份证号", max_length=18, help_text="18位有效身份证号")
    email = models.EmailField()
    sexChoices = [
        ('m', '男',),
        ('w', '女',),
    ]
    sex = models.CharField(verbose_name="性别", max_length=1, choices=sexChoices)
    security_question_choices = [
        ('name', '您目前的姓名是?',),
        ('spouse', '您配偶的姓名是?',),
        ('id', '您的学号(工号)是?',),
        ('mother', '您母亲的姓名是?',),
        ('father', '您父亲的姓名是?',),
        ('friend', '您最好的朋友姓名是?',),
    ]
    security_question = models.CharField(verbose_name="密保问题", max_length=10, default='name', db_index=True,
                                         choices=security_question_choices)
    answer = models.CharField(verbose_name="密保问题答案", max_length=20, help_text="最长不超过20个字符", default="", db_index=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
