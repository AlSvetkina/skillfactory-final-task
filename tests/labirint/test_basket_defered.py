from pages.labirint import MainPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


def test_book_deffered_page_add_book(web_browser):
    """ Make sure that we can mark book as a deffered. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    assert 'active' not in elem.get_attribute('class')

    elem.click()

    assert 'active' in elem.get_attribute('class')


def test_book_deffered_page_menu(web_browser):
    """ Make sure that we can open deffered menu for a book. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    assert page.elements(
        class_name="js-putorder-block-change")[0].is_displayed()

    time.sleep(10)


def test_book_deffered_page(web_browser):
    """ Make sure that we can mark book as deffered and see it
        on deffered page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()

    book_id = elem.get_attribute("data-id_book")

    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    assert page.get_current_url() == f'{page._base_url}/cabinet/putorder/'
    assert page.elements(class_name="product")[0].get_attribute(
        "data-product-id") == book_id


def test_book_deffered_page_clear(web_browser):
    """ Make sure that we can clean deffered list. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    assert page.elements(class_name="product").count() == 1

    page.elements(class_name="btn-clear-blue")[1].click()

    assert page.elements(class_name="product").count() == 0


def test_book_deffered_page_preview(web_browser):
    """ Make sure that preview for a book works on defferend page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    elem = page.elements(class_name="product")[0]

    elem.click()

    time.sleep(1)

    assert page.element(id="cart-preview").is_visible()


def test_book_deffered_page_preview_close(web_browser):
    """ Make sure that we can close preview of a book on deffered page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    elem = page.elements(class_name="product")[0]

    elem.click()

    time.sleep(1)

    preview = page.element(id="cart-preview")

    assert preview.is_visible()

    ActionChains(web_browser).send_keys(Keys.ESCAPE).perform()

    assert not preview.is_visible()


def test_book_deffered_page_select_page(web_browser):
    """ Make sure that we can select a book on deffered page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    elem = page.elements(class_name="product")[0]

    assert 'product-m-checked' not in elem.get_attribute('class')

    page.elements(class_name="btn-clear-blue")[0].click()

    assert 'product-m-checked' in elem.get_attribute('class')


def test_book_deffered_page_select_all_page(web_browser):
    """ Make sure that we can select all books on deffered page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()

    elem = page.elements(class_name="js-open-deferred-block")[1]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    page.elements(class_name="btn-clear-blue")[0].click()

    assert page.elements(class_name="product").count() == 2

    for elem in page.elements(class_name="product"):
        assert 'product-m-checked' in elem.get_attribute('class')


def test_book_deffered_page_select_all_and_move_to_basket(web_browser):
    """ Make sure that we can move books to the basket. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()

    elem = page.elements(class_name="js-open-deferred-block")[1]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    page.elements(class_name="btn-clear-blue")[0].click()

    products = page.elements(class_name="product")

    assert products.count() == 2

    assert not page.elements(
        class_name="b-basket-popinfo-e-text-m-add")[0].is_displayed()

    page.elements(class_name="js-ap-btn-main")[0].click()

    assert page.elements(
        class_name="b-basket-popinfo-e-text-m-add").count() == 0


def test_book_deffered_page_select_all_and_move_to_basket_and_confirm(web_browser):
    """ Make sure that we can move books to the basket and confirm. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()

    elem = page.elements(class_name="js-open-deferred-block")[1]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    page.elements(class_name="btn-clear-blue")[0].click()

    products = page.elements(class_name="product")

    assert products.count() == 2

    ids = []
    for elem in products:
        ids.append(elem.get_attribute('data-product-id'))

    page.elements(class_name="js-ap-btn-main")[0].click()

    alert = web_browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    page.elements(class_name="basket-go")[0].click()

    assert page.get_current_url() == f'{page._base_url}/cart/'

    for elem in page.elements(class_name="product_labeled"):
        assert elem.get_attribute('data-product-id') in ids


def test_book_deffered_page_select_all_deselect_all_page(web_browser):
    """ Make sure that we can select all and deselect all
        books on deffered page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()

    elem = page.elements(class_name="js-open-deferred-block")[1]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    assert page.elements(class_name="product").count() == 2

    for elem in page.elements(class_name="product"):
        assert 'product-m-checked' not in elem.get_attribute('class')

    page.elements(class_name="btn-clear-blue")[0].click()

    assert 'product-m-checked' in elem.get_attribute('class')
    for elem in page.elements(class_name="product"):
        assert 'product-m-checked' in elem.get_attribute('class')

    page.elements(class_name="js-ap-btn-cancel")[0].click()

    for elem in page.elements(class_name="product"):
        assert 'product-m-checked' not in elem.get_attribute('class')


def test_book_deffered_page_select_all_and_delete_all(web_browser):
    """ Make sure that we can select all and delete all
        books from deffered list. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()

    elem = page.elements(class_name="js-open-deferred-block")[1]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    assert page.elements(class_name="product").count() == 2

    for elem in page.elements(class_name="product"):
        assert 'product-m-checked' not in elem.get_attribute('class')

    page.elements(class_name="btn-clear-blue")[0].click()

    page.elements(class_name="js-ap-btn-remove")[0].click()

    assert page.elements(class_name="product").count() == 0


def test_book_deffered_page_select_and_deselect_page(web_browser):
    """ Make sure that we can select and deselect a
        book in the deffered list. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    elem = page.elements(class_name="product")[0]

    page.elements(class_name="btn-clear-blue")[0].click()

    assert 'product-m-checked' in elem.get_attribute('class')

    page.elements(class_name="b-checkbox-m-radius")[0].click()

    assert 'product-m-checked' not in elem.get_attribute('class')


def test_book_deffered_page_header_icon(web_browser):
    """ Make sure that top header deffered icon is
        in sync with deffered list. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()

    time.sleep(1)

    assert page.elements(
        class_name="b-header-b-personal-e-icon-count-m-putorder")[0].text == "1"


def test_book_deffered_page_header_icon_to_putorder(web_browser):
    """ Make sure that top header icon link goes to deffered page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    id = elem.get_attribute("data-id_book")

    elem.click()

    page.elements(class_name="top-link-main_putorder")[0].click()

    assert page.get_current_url() == f'{page._base_url}/cabinet/putorder/'

    product_cart = page.elements(class_name="product-cart")[0]

    assert id == product_cart.get_attribute("data-product-id")


def test_book_deffered_page_header_icon_to_basket_putorder(web_browser):
    """ Make sure that deffered books displays in basket. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    id = elem.get_attribute("data-id_book")

    elem.click()

    page.elements(class_name="cart-icon-js")[0].click()

    assert page.get_current_url() == f'{page._base_url}/cart/'

    page.elements(class_name="ui-tabs-anchor")[1].click()

    assert not page.element(id="step1-default").is_visible()

    product_cart = page.elements(class_name="product-cart")[0]

    assert id == product_cart.get_attribute("data-product-id")


def test_book_deffered_page_header_icon_to_basket_putorder_move_to_basket(web_browser):
    """ Make sure that we can move defferd books to basket on basket page. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    id = elem.get_attribute("data-id_book")

    elem.click()

    page.elements(class_name="cart-icon-js")[0].click()

    assert page.get_current_url() == f'{page._base_url}/cart/'

    page.elements(class_name="ui-tabs-anchor")[1].click()

    page.elements(class_name="js-buy-wishlist")[0].click()

    alert = web_browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    assert page.element(id="step1-default").is_visible()

    product_cart = page.elements(class_name="product-cart")[0]

    assert id == product_cart.get_attribute("data-product-id")
