"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# coding: uft-8
from django.contrib import admin
from django.urls import path, include
from app.client import urls as client_urls
from app.dashboard import urls as dashboard_urls

urlpatterns = [
    path('admin/', admin.site.urls), # 并不使用自带的admin,可以去掉
    path('dashboard/', include(dashboard_urls)),
    path('client/', include(client_urls))
]
