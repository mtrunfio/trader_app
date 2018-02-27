#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# navbar.py
# @Author : Mauricio Trunfio (omnipumbs@gmail.com)
# @Link   : https://github.com/mtrunfio
# @Date   : 2/26/2018, 8:21:52 PM
from django import template

register = template.Library()


@register.inclusion_tag('includes/_navbar.html')
def show_navbar():
    return {}