# coding: utf-8

from django.views.generic import View
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth

class Index(View):
    TEMPLATE = 'dashboard/index.html'

    # 这里进行用户验证的时候,当没有登录的时候,会循环重定向,会出现问题,自己没有解决,会有这问题,但是后来又好了
    @dashboard_auth
    def get(self, request):
        return render_to_response(request, self.TEMPLATE)