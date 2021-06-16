# coding: utf-8

import functools
from django.shortcuts import redirect, reverse

# 对用户进行登录验证
def dashboard_auth(func):

    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):

        user = request.user
        if not user.is_authenticated or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('dashboard_login'), request.path))

        return func(self, request, *args, **kwargs)
    return wrapper