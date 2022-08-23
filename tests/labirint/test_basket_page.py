from pages.labirint import MainPage

import time


def test_put_one_in_basket(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()

    basket = page.elements(class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "1"


def test_put_twice_the_same_in_basket(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "1"

    buy_links[0].click()

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "1"
    time.sleep(1)

    assert page.get_current_url() == f'{page._base_url}/cart/'


def test_put_twice_different_in_basket(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "1"

    buy_links[1].click()

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "2"
