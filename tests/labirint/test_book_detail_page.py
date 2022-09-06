from pages.labirint import MainPage, DetailPage

import time


def test_book_details_from_main_page(web_browser):
    """ Make sure that link from a book leads to right details page.  """

    page = DetailPage(web_browser)
    assert page.get_current_url() == f'{page._base_url}/books/{page.book_id}/'

    book = page.element(id="product-info")
    assert page.book_id == book.get_attribute("data-product-id")


def test_book_details_page_book_add_to_basket(web_browser):
    """ Make sure that we can add the book to the basket
        from details page. """

    page = DetailPage(web_browser)

    page.elements(class_name="btn-buy")[0].click()

    time.sleep(1)

    page.elements(class_name="tobasket")[0].click()

    assert page.wait_for_url('cart/')

    product_cart = page.element(class_name="product-cart")

    assert page.book_id == product_cart.get_attribute("data-product-id")

    quantity = page.element(class_name="quantity")
    assert quantity.get_attribute('value') == "1"


def test_book_details_page_defered(web_browser):
    """ Make sure that we can add the book to the deffered list
        from details page. """

    page = DetailPage(web_browser)

    fave_btn = page.element(class_name="fave")
    fave_btn.click()
    fave_btn.click()

    assert page.wait_for_url('cabinet/putorder/')

    product_cart = page.element(class_name="watched")

    assert page.book_id == product_cart.get_attribute("data-product-id")


def test_book_details_page_compare(web_browser):
    """ Make sure that we can compare a book on details page. """

    page = DetailPage(web_browser)

    btn_compare = page.element(class_name="big-compare")
    btn_compare.click()
    btn_compare.click()

    assert page.wait_for_url('compare/')

    product_cart = page.element(class_name="compare-main__column")

    assert page.book_id == product_cart.get_attribute("data-product-id")

