#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    _base_url = None

    def __init__(self, web_driver, url=''):
        self._base_url = 'https://www.labirint.ru'
        super().__init__(web_driver, self._base_url + url)

        self.search = self.element(id='search-field')

        policy = self.elements(class_name="js-cookie-policy-agree")
        if policy.count() == 1:
            policy[0].click()


    def get_search_suggestions(self):
        return self.elements(class_name="b-suggests-e-item-name")
