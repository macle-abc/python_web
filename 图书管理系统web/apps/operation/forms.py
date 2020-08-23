from typing import Dict

from django import forms
from django.forms import ModelForm
from .models import UserInfo


class LoginForm(forms.Form):
    #     error_messages={'required': '密码不能为空'},
    account = forms.CharField(required=True, max_length=13, min_length=6)
    password = forms.CharField(required=True, max_length=18, min_length=6)


from django.utils.translation import gettext_lazy as _


# class RegisterForm(forms.Form):
#         account  = forms.CharField(required=True, max_length=20, min_length=10, error_messages={"min_length": "长度问题"})
class RegisterForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        error_messages = {
            "account": {
                "unique": "该账号已经存在",
            }
        }


class ForgotPasswordForm(ModelForm):
    pass


class ReaderWishForm(forms.Form):
    name = forms.CharField(required=True, max_length=30)
    author = forms.CharField(required=True, max_length=20)
    other = forms.CharField(required=True)


class SuggestForm(forms.Form):
    name = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(required=True)
    suggest = forms.CharField(required=True, max_length=200)
