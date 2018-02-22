#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# t3.py
# @Author : Mauricio Trunfio (omnipumbs@gmail.com)
# @Link   : https://github.com/mtrunfio
# @Date   : 2/21/2018, 3:54:12 PM

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    #/dashboard/
    url(r'^$', views.HomeView.as_view(), name='home'),
    #path("", views.index, name='index'),
]
