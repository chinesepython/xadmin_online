# -*- coding: utf-8 -*-
__author__ = 'xyh'
__date__ = '2019/4/9 15:28'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    # 字段和前端保持一致
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()
