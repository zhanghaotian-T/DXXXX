#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: urls.py
@time: 2022/02/08
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]