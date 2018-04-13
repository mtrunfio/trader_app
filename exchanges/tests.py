#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# t3.py
# @Author : Mauricio Trunfio (omnipumbs@gmail.com)
# @Link   : https://github.com/mtrunfio
# @Date   : 2/21/2018, 3:54:12 PM

from django.test import TestCase
from exchanges.models import Exchange

# Create your tests here.


class ExchangeModelTests(TestCase):
    app = Exchange()

    def test_add_exchange(self):
        """
        add_exchange() returns an Exchange object if it added.

        """
        exchange_name = "Testing"
        api_key = "Testing"
        secret = "Testing"
        new_exchange = self.app.add_exchange(exchange_name, api_key, secret)
        self.assertIs(new_exchange.exchange_name, "Testing")

    def test_add_exchange_empty_name(self):
        """
        add_exchange() returns an error if exchange_name is empty.

        """
        exchange_name = ""
        api_key = "Testing"
        secret = "Testing"
        new_exchange = self.app.add_exchange(exchange_name, api_key, secret)
        self.assertEqual(new_exchange["statuscode"], 0x1001)

    def test_add_exchange_empty_api(self):
        """
        add_exchange() returns an error if api_key is empty.

        """
        exchange_name = "Testing"
        api_key = ""
        secret = "Testing"
        new_exchange = self.app.add_exchange(exchange_name, api_key, secret)
        self.assertIn(new_exchange[0], "error")

    def test_add_exchange_empty_secret(self):
        """
        add_exchange() returns an error if secret is empty.

        """
        exchange_name = "Testing"
        api_key = "Testing"
        secret = ""
        new_exchange = self.app.add_exchange(exchange_name, api_key, secret)
        self.assertIn(new_exchange[0], "error")

    def test_delete_exchange(self):
        """
        add_exchange() returns an error if exchange_name is empty.

        """
        new_exchange = self.app.add_exchange("test", "test", "test")
        ret = self.app.delete_exchange(new_exchange.id)
        self.assertIn(ret[0], "success")

    def test_delete_exchange_not_exists(self):
        """
        add_exchange() returns an error if exchange_name is empty.

        """
        ret = self.app.delete_exchange(20)
        self.assertIn(ret[0], "error")

    def test_update_exchange(self):
        """
        add_exchange() returns an error if exchange_name is empty.

        """
        new_exchange = self.app.add_exchange("test", "test", "test")
        values = {"exchange_name": "111", "api_key": "111", "secret": "111"}
        ret = self.app.update_exchange(new_exchange.id, values)
        self.assertIn(ret[0], "success")

    def test_update_exchange_not_exists(self):
        """
        add_exchange() returns an error if exchange_name is empty.

        """
        values = {"exchange_name": "111", "api_key": "111", "secret": "111"}
        ret = self.app.update_exchange(20, values)
        self.assertIn(ret[0], "error")

    def test_update_exchange_value_empty(self):
        """
        add_exchange() returns an error if exchange_name is empty.

        """
        new_exchange = self.app.add_exchange("test", "test", "test")
        values = {"exchange_name": "", "api_key": "111", "secret": "111"}
        ret = self.app.update_exchange(new_exchange.id, values)
        self.assertIn(ret[0], "error")
