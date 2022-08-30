from pages.labirint import MainPage

import time


def test_put_one_in_basket(web_browser):
    """ Make sure that we can put a book in a basket and
        top bar icon will be in sync. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()

    basket = page.elements(class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "1"


def test_put_twice_the_same_in_basket(web_browser):
    """ Make sure that we can put the same book twice in the basket. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()

    time.sleep(1)

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
    """ Make sure that we can put two different book in the basket. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()

    time.sleep(1)

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "1"

    buy_links[1].click()

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "2"


def test_add_to_basket_and_check_quantity(web_browser):
    """ Make sure that quantity is correct on the basket page. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()
    buy_links[0].click()

    time.sleep(1)

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "1"


def test_add_to_basket_and_increase(web_browser):
    """ Make sure that we can increase quantity on the basket page. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()
    buy_links[0].click()

    time.sleep(1)

    btn_increase = page.elements(class_name="btn-increase")[0]
    btn_increase.click()

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "2"

    btn_increase.click()

    assert quantity.get_attribute('value') == "3"


def test_add_to_basket_and_decrease(web_browser):
    """ Make sure that we can increase/decrease quantity on the basket page. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()
    buy_links[0].click()

    time.sleep(1)

    btn_increase = page.elements(class_name="btn-increase")[0]
    btn_increase.click()
    btn_increase.click()

    time.sleep(1)

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "3"

    btn_lessen = page.elements(class_name="btn-lessen")[0]
    btn_lessen.click()
    time.sleep(1)

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "2"

    btn_lessen = page.elements(class_name="btn-lessen")[0]
    btn_lessen.click()

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "1"

    btn_lessen = page.elements(class_name="btn-lessen")[0]
    btn_lessen.click()

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "0"


def test_add_and_clean_basket(web_browser):
    """ Make sure that we can clean the basket list. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()
    buy_links[0].click()

    time.sleep(1)

    empty_basket_link = page.elements(class_name="empty-basket-link")[0]
    empty_basket_link.click()

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "0"


def test_add_and_clean_and_restore_basket(web_browser):
    """ Make sure that we can restore the basket list. """

    page = MainPage(web_browser, url='/')

    buy_links = page.elements(class_name="buy-link")

    buy_links[0].click()
    buy_links[0].click()

    time.sleep(1)

    empty_basket_link = page.elements(class_name="empty-basket-link")[0]
    empty_basket_link.click()

    basket = page.elements(
        class_name="b-header-b-personal-e-icon-count-m-cart")[0]
    assert basket.text == "0"

    restore_link = page.elements(class_name="empty-basket-link")[0]
    restore_link.click()

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "1"
