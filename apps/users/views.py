from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .forms import LoginForm, RegisterForm


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 使username可以传入用户名和邮箱
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        # 后端对于前端提交的表格内容进行验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            return render(request, 'login.html', context={"msg": "用户名或者密码输入错误"})

        else:
            return render(request, 'login.html', context={"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        regisger_form = RegisterForm(request.POST)
        if regisger_form.is_valid():
            pass

        pass

# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, 'login.html', context={"msg": "用户名或者密码输入错误"})
#     elif request.method == "GET":
#         return render(request, "login.html", {})












































































































































































































