#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# t3.py
# @Author : Mauricio Trunfio (omnipumbs@gmail.com)
# @Link   : https://github.com/mtrunfio
# @Date   : 2/21/2018, 3:54:12 PM

from django.urls import path

from . import views

app_name = 'exchanges'
urlpatterns = [
    #/exchanges/
    path("", views.index, name='index'),
    #ex: /exchanges/1/
    path('<int:exchange_id>/', views.detail, name='detail')
]