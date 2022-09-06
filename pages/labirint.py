#!/usr/bin/python3
# -*- encoding=utf8 -*-

from pages.base import WebPage


class MainPage(WebPage):

    _base_url = None

    def __init__(self, web_driver, url=''):
        self._base_url = 'https://www.labirint.ru'
        super().__init__(web_driver, self._base_url + url)
        #  element = self.web_driver.execute_script(
            #  "return document.querySelector('body').querySelector('[class=\"js-cookie-policy-agree\"]')")
        #  print('element=', element)

        self.search = self.element(id='search-field')

        cookie_policy = self.element(
            class_name="js-cookie-policy-agree").find(timeout=1)
        if cookie_policy:
            cookie_policy.click()


    def get_search_suggestions(self):
        return self.elements(class_name="b-suggests-e-item-name")
