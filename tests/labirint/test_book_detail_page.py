from pages.labirint import MainPage

import time


def test_main_page_book_details(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    book = page.elements(class_name="product")[0]
    id = book.get_attribute("data-product-id")

    book.click()

    assert page.get_current_url() == f'{page._base_url}/books/{id}/'

    book = page.elements(class_name="product")[0]
    assert id == book.get_attribute("data-product-id")


def test_book_details_page_book_add_to_basket(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    book = page.elements(class_name="product")[0]
    id = book.get_attribute("data-product-id")

    book.click()

    page.elements(class_name="btn-buy")[0].click()

    time.sleep(1)

    page.elements(class_name="tobasket")[0].click()

    product_cart = page.elements(class_name="product-cart")[0]

    assert id == product_cart.get_attribute("data-product-id")

    quantity = page.elements(class_name="quantity")[0]
    assert quantity.get_attribute('value') == "1"


def test_book_details_page_defered(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    book = page.elements(class_name="product")[0]
    id = book.get_attribute("data-product-id")

    book.click()

    page.elements(class_name="fave")[0].click()
    page.elements(class_name="fave")[0].click()

    product_cart = page.elements(class_name="product-cart")[0]

    assert id == product_cart.get_attribute("data-product-id")


def test_book_details_page_compare(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    book = page.elements(class_name="product")[0]
    id = book.get_attribute("data-product-id")

    book.click()

    btn_compare = page.elements(class_name="big-compare")[0]
    btn_compare.click()
    btn_compare.click()

    assert page.get_current_url() == f'{page._base_url}/compare/'

    product_cart = page.elements(class_name="compare-main__column")[0]

    assert id == product_cart.get_attribute("data-product-id")

