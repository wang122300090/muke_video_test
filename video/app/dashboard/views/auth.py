# coding: utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse
from app.libs.base_render import render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator  # 分页
from app.utils.permission import dashboard_auth
from app.models import ClientUser
from django.http import JsonResponse



class Login(View):
    TEMPLATE = 'dashboard/auth/login.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))
        to = request.GET.get('to', '')

        data = {}
        data = {'error': '', 'to': to}
        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        to = request.GET.get('to', '')
        # print(username, password)
        data = {}
        exists = User.objects.filter(username=username).exists()
        data['error'] = '没有该用户'
        if not exists:
            return render_to_response(request, self.TEMPLATE, data=data)
        user = authenticate(username=username, password=password)
        if not user:
            data['error'] = '密码错误'
            return render_to_response(request, self.TEMPLATE, data=data)
        if not user.is_superuser:
            data['error'] = '你无权登录'
            return render_to_response(request, self.TEMPLATE, data=data)
        login(request, user)
        if to:
            return redirect(to)
        return redirect(reverse('dashboard_index'))


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('dashboard_login'))


class AdminManager(View):

    TEMPLATE = 'dashboard/auth/admin.html'

    @dashboard_auth
    def get(self, request):
        # users = User.objects.filter(is_superuser=True)  # 拿到所有的superuser
        users = User.objects.all()  # 拿到所有的user
        page = request.GET.get('page', 1)
        p = Paginator(users, 2)
        total_page = p.num_pages
        if int(page) <= 1:
            page = 1
        current_page = p.get_page(int(page)).object_list

        # print(current_page) # 拿到当前页的用户数
        data = {'users': current_page, 'total': total_page, 'page_num': int(page)}
        return render_to_response(request, self.TEMPLATE, data)


class UpdateAdminStatus(View):

    def get(self, request):
        status = request.GET.get('status', 'on')

        _status = True if status == 'on' else False
        # request.user.is_superuser = _status
        # request.user.save()
        user_id = request.GET.get('user_id')
        user = User.objects.filter(id=user_id)
        user.update(is_superuser=_status)
        return redirect(reverse('admin_manager'))
    # 这里是老师发生错误了,应该需要传入用户的id


class ClientManager(View):
    TEMPLATE = 'dashboard/auth/client_user.html'

    def get(self, request):

        users = ClientUser.objects.all()
        data = {'users': users}
        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        user_id = request.POST.get('userId')
        user = ClientUser.objects.get(pk=user_id)
        print(user)
        user.update_status()
        # 这里用ajax,否则就需要重写get方法,也可以修改get方法
        return JsonResponse({'code': 0, 'msg': 'success'})


