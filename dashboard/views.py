#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# t3.py
# @Author : Mauricio Trunfio (omnipumbs@gmail.com)
# @Link   : https://github.com/mtrunfio
# @Date   : 2/21/2018, 3:54:12 PM

from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    template_name = 'index.html'
