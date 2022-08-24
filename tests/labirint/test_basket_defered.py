from pages.labirint import MainPage

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

    page.elements(class_name="btn-clear-blue").click()

    assert page.elements(class_name="product").count() == 0

#  def test_add_book_to_compare(web_browser):
    #  """ Make sure main search works fine. """
    #  web_browser.set_window_size(1280, 1024)

    #  page = MainPage(web_browser, url='/')
    #  page.elements(class_name="icon-compare")[0].click()

    #  compare = page.elements(class_name="js-card-block-actions-compare")[0]
    #  compare.click()

    #  assert compare.text == "Перейти к сравнению"


#  def test_add_book_to_compare_and_close_menu(web_browser):
    #  """ Make sure main search works fine. """
    #  web_browser.set_window_size(1280, 1024)

    #  page = MainPage(web_browser, url='/')
    #  page.elements(class_name="icon-compare")[0].click()

    #  compare = page.elements(class_name="js-card-block-actions-compare")[0]
    #  compare.click()

    #  page.send_escape()

    #  assert not compare.is_displayed()


#  def test_add_two_and_compare(web_browser):
    #  """ Make sure main search works fine. """
    #  page = MainPage(web_browser, url='/')
    #  web_browser.execute_script("window.scrollBy(0,500)")

    #  page.elements(class_name="icon-compare")[0].click()

    #  compare_1 = page.elements(class_name="icon-compare")[0]
    #  book_title_1 = compare_1.get_attribute("data-title")

    #  compare_2 = page.elements(class_name="icon-compare")[1]
    #  book_title_2 = compare_2.get_attribute("data-title")

    #  assert book_title_1 != book_title_2

    #  compare_1.click()
    #  compare_1 = page.elements(class_name="js-card-block-actions-compare")[0]
    #  compare_1.click()
    #  page.send_escape()

    #  compare_2.click()
    #  compare_2 = page.elements(class_name="js-card-block-actions-compare")[0]
    #  compare_2.click()
    #  compare_2.click()

    #  assert page.get_current_url() == f'{page._base_url}/compare/'
    #  assert page.elements(class_name="item-name__href").count() == 2
    #  #  items = page.elements(class_name="item-name__href")
    #  #  assert items[0].text == book_title_1
    #  #  assert items[1].text == book_title_2


#  def test_add_two_and_compare_and_cancel(web_browser):
    #  """ Make sure main search works fine. """
    #  page = MainPage(web_browser, url='/')
    #  web_browser.execute_script("window.scrollBy(0,500)")

    #  page.elements(class_name="icon-compare")[0].click()

    #  compare_1 = page.elements(class_name="icon-compare")[0]
    #  compare_1.click()
    #  compare_1 = page.elements(class_name="js-card-block-actions-compare")[0]
    #  compare_1.click()
    #  page.send_escape()

    #  compare_2 = page.elements(class_name="icon-compare")[1]
    #  compare_2.click()
    #  compare_2 = page.elements(class_name="js-card-block-actions-compare")[0]
    #  compare_2.click()
    #  compare_2.click()

    #  page.elements(class_name="compare-delete-list__text")[0].click()

    #  assert page.elements(class_name="item-name__href").count() == 0
