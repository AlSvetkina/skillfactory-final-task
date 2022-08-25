from pages.labirint import MainPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time


def test_add_book_to_deffered(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    assert 'active' not in elem.get_attribute('class')

    elem.click()

    assert 'active' in elem.get_attribute('class')


def test_book_deffered_menu(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    assert page.elements(
        class_name="js-putorder-block-change")[0].is_displayed()


def test_book_deffered_page(web_browser):
    """ Make sure main search works fine. """

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


def test_book_deffered_clear_page(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    assert page.elements(class_name="product").count() == 1

    page.elements(class_name="btn-clear-blue")[1].click()

    assert page.elements(class_name="product").count() == 0


def test_book_deffered_preview(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    elem = page.elements(class_name="product")[0]

    elem.click()

    assert page.element(id="cart-preview").is_visible()


def test_book_deffered_preview_close(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    elem = page.elements(class_name="product")[0]

    elem.click()

    preview = page.element(id="cart-preview")

    assert preview.is_visible()

    ActionChains(web_browser).send_keys(Keys.ESCAPE).perform()

    assert not preview.is_visible()


def test_book_deffered_select_page(web_browser):
    """ Make sure main search works fine. """

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


def test_book_deffered_select_all_page(web_browser):
    """ Make sure main search works fine. """

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


def test_book_deffered_select_all_deselect_all_page(web_browser):
    """ Make sure main search works fine. """

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

    policy = page.elements(class_name="js-cookie-policy-agree")
    if policy.count() == 1:
        policy[0].click()

    page.elements(class_name="js-ap-btn-cancel")[0].click()

    for elem in page.elements(class_name="product"):
        assert 'product-m-checked' not in elem.get_attribute('class')

def test_book_deffered_select_all_and_delete_all(web_browser):
    """ Make sure main search works fine. """

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


def test_book_deffered_select_and_deselect_page(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    elem = page.elements(class_name="js-open-deferred-block")[0]

    elem.click()
    elem.click()

    page.elements(
        class_name="b-list-item-hover")[0].click()

    elem = page.elements(class_name="product")[0]

    page.elements(class_name="btn-clear-blue")[0].click()

    assert 'product-m-checked' in elem.get_attribute('class')

    elem.click()

    assert 'product-m-checked' not in elem.get_attribute('class')
