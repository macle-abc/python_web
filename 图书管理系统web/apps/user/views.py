from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View

from ..operation.views import get_cookies_isLogin_context
from .models import UserInfo
from .forms import UserInfoForm, UserInfoSafeForm


class UserCenterView(View):
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
                    # 成功
                    return render(request, "center.html", context)
            else:
                return redirect("operation:login")
        else:
            return redirect("operation:login")

    def post(self, request, *args, **kwargs):
        cookies = request.COOKIES
        if 'account' in cookies:
            account = cookies['account']
        else:
            return redirect("user:center")
        if 'type' in kwargs and kwargs['type'] == 'user':
            userInfo = UserInfo.objects.get(account=account)
            mf = UserInfoForm(request.POST, request.FILES, instance=userInfo)
            if mf.is_valid():
                mf.save()
                return render(request, "tips.html", {"message": "信息修改成功!", "url": "/usercenter/center"})
            else:
                return redirect("user:center")
        elif 'type' in kwargs and kwargs['type'] == 'safe':
            newUserInfo = UserInfoSafeForm(request.POST)
            if newUserInfo.is_valid():
                # 检查是否需要修改密码
                userInfo = UserInfo.objects.get(account=account)
                if newUserInfo.cleaned_data['oldpassword'] and newUserInfo.cleaned_data['newpassword']:
                    # 需要修改密码
                    # 验证密码
                    if userInfo.password == newUserInfo.cleaned_data['oldpassword']:
                        # 进行修改
                        userInfo.password = newUserInfo.cleaned_data['newpassword']
                        userInfo.security_question = newUserInfo.cleaned_data[
                            'security_question'] if newUserInfo.cleaned_data[
                            'security_question'] else userInfo.security_question
                        userInfo.answer = newUserInfo.cleaned_data['answer'] if newUserInfo.cleaned_data[
                            'answer'] else userInfo.answer
                        userInfo.save()
                        response = render_to_response("tips.html",
                                                      {"message": "修改成功!请重新登录!", "url": '/operation/login/'})
                        response.delete_cookie('isLogin')
                        response.delete_cookie('account')
                        return response
                    else:
                        return redirect("user:center")
                else:
                    userInfo.security_question = newUserInfo.cleaned_data[
                        'security_question'] if newUserInfo.cleaned_data[
                        'security_question'] else userInfo.security_question
                    userInfo.answer = newUserInfo.cleaned_data['answer'] if newUserInfo.cleaned_data[
                        'answer'] else userInfo.answer
                    userInfo.save()
                    return render(request, "tips.html",
                                  {"message": "修改成功!", "url": '/usercenter/'})
            else:
                return redirect("user:center")
        else:
            return redirect("user:center")


# class UserRentalView(View):
#     def get(self, request, *args, **kwargs):
#         result = get_cookies_isLogin_context(request)
#         cookies = result[0]
#         context = result[2]
#         if cookies:
#             if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
#                 context['isLogin'] = True
#                 account = cookies['account']
#                 # 获取用户信息
#                 try:
#                     userInfo = UserInfo.objects.get(account=account)
#                 except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
#                     return redirect("operation:login")
#                 else:
#                     context['userInfo'] = userInfo
#                     # 判断id
#                     if 'page' in kwargs:
#                         page = kwargs['page']
#                     else:
#                         page = 1
#                     print(page)
#                     # 分页实现
#                     # 判断如果条数不足10那么不显示分页
#                     # 成功/*
#                     return render(request, "rental.html", context)
#             else:
#                 return redirect("operation:login")
#         else:
#             return redirect("operation:login")


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        # response = redirect("operation:index")
        # response.delete_cookie("isLogin")
        response = render_to_response("tips.html", {"message": "注销成功!", "url": "/operation/index"})
        response.delete_cookie("isLogin")
        response.flush()
        return response
