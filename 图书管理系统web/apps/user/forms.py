from django.forms import ModelForm
from django import forms

from .models import UserInfo


class UserInfoSafeForm(forms.Form):
    security_question = forms.CharField(max_length=10, required=False)
    answer = forms.CharField(max_length=20, required=False)
    oldpassword = forms.CharField(max_length=12, min_length=6, required=False)
    newpassword = forms.CharField(max_length=12, min_length=6, required=False)


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'account':
                self.fields[field].required = False

    # 头像
    # 昵称
    # 邮箱
    # 身份证号
    # 性别
    # 密保问题
    # 答案
    # 新密码
