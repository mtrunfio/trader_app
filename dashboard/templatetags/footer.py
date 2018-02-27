#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# footer.py
# @Author : Mauricio Trunfio (omnipumbs@gmail.com)
# @Link   : https://github.com/mtrunfio
# @Date   : 2/26/2018, 8:46:51 PM
from django import template

register = template.Library()


@register.inclusion_tag('includes/_footer.html')
def show_footer():
    return {}