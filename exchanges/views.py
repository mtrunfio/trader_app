#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# t3.py
# @Author : Mauricio Trunfio (omnipumbs@gmail.com)
# @Link   : https://github.com/mtrunfio
# @Date   : 2/21/2018, 3:54:12 PM

from django.shortcuts import get_object_or_404, render
# Create your views here.

from .models import Exchange


def index(request):
    exchange_list = Exchange.objects.order_by('id')
    context = {'exchange_list': exchange_list}
    return render(request, 'exchanges/index.html', context)


def detail(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    return render(request, 'exchanges/detail.html', {'exchange': exchange})

