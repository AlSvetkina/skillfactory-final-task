from pages.labirint import MainPage

import time


def test_check_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser, url='/')

    page.search.set_value("Букварь")
    suggestions = page.get_search_suggestions()

    assert suggestions.count() == 5


def test_check_wrong_input_in_search(web_browser):
    page = MainPage(web_browser, url='/')

    page.search.set_value(",erdfhm")
    suggestions = page.get_search_suggestions()

    assert suggestions.count() == 5


def test_check_search_cancelation(web_browser):
    page = MainPage(web_browser, url='/')

    page.search.set_value(",erdfhm")
    page.send_escape()

    suggestions_block = page.element(id="autohelp_rows")

    assert not suggestions_block.is_visible()


def test_check_top_header_books(web_browser):
    """ Make sure that link to books page works """

    page = MainPage(web_browser, url='/')

    top_bar_element = 0
    top_header = page.elements(class_name="b-header-b-menu-e-text")
    href = top_header[top_bar_element].get_attribute('href')
    top_header[top_bar_element].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_top_header_main_books(web_browser):
    """ Make sure that link to main books page works """

    page = MainPage(web_browser, url='/')

    top_bar_element = 1
    top_header = page.elements(class_name="b-header-b-menu-e-text")
    href = top_header[top_bar_element].get_attribute('href')
    top_header[top_bar_element].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_top_header_school(web_browser):
    """ Make sure that link to school page works """

    page = MainPage(web_browser, url='/')

    top_bar_element = 2
    top_header = page.elements(class_name="b-header-b-menu-e-text")
    href = top_header[top_bar_element].get_attribute('href')
    top_header[top_bar_element].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_top_header_toys(web_browser):
    """ Make sure that link to toys page works """

    page = MainPage(web_browser, url='/')

    top_bar_element = 3
    top_header = page.elements(class_name="b-header-b-menu-e-text")
    href = top_header[top_bar_element].get_attribute('href')
    top_header[top_bar_element].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_top_header_office(web_browser):
    """ Make sure that link to office page works """

    page = MainPage(web_browser, url='/')

    top_bar_element = 4
    top_header = page.elements(class_name="b-header-b-menu-e-text")
    href = top_header[top_bar_element].get_attribute('href')
    top_header[top_bar_element].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_top_header_house_hold(web_browser):
    """ Make sure that link to house hould works on small screen """
    web_browser.set_window_size(960, 540)

    page = MainPage(web_browser, url='/')

    top_bar_element = 5
    top_header = page.elements(class_name="b-header-b-menu-e-text")
    href = top_header[top_bar_element].get_attribute('href')
    top_header[top_bar_element].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_sub_header_help(web_browser):
    """ Make sure that link to help works on big screen """
    page = MainPage(web_browser, url='/')

    sub_header_index = 0
    sub_header = page.elements(class_name="b-header-b-sec-menu-e-link")
    href = sub_header[sub_header_index].get_attribute('href')
    sub_header[sub_header_index].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_sub_header_certeficates(web_browser):
    """ Make sure that link to certeficates works on big screen """
    page = MainPage(web_browser, url='/')

    sub_header_index = 1
    sub_header = page.elements(class_name="b-header-b-sec-menu-e-link")
    href = sub_header[sub_header_index].get_attribute('href')
    sub_header[sub_header_index].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_sub_header_ratings(web_browser):
    """ Make sure that link to ratings works on big screen """
    page = MainPage(web_browser, url='/')

    sub_header_index = 2
    sub_header = page.elements(class_name="b-header-b-sec-menu-e-link")
    href = sub_header[sub_header_index].get_attribute('href')
    sub_header[sub_header_index].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_check_sub_header_novelty(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    sub_header_index = 3
    sub_header = page.elements(class_name="b-header-b-sec-menu-e-link")
    href = sub_header[sub_header_index].get_attribute('href')
    sub_header[sub_header_index].click()
    time.sleep(1)

    assert page.get_current_url() == href


def test_main_page_gallery_next(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    carousel_items = page.elements(class_name="jcarousel-item")

    carousel_items_1 = carousel_items[0]

    assert carousel_items_1.is_displayed()

    product = page.elements(class_name="product_labeled")[0]

    assert product.is_displayed()

    arrow_right = page.element(class_name="carousel-arrow-right")
    arrow_right.click()

    time.sleep(1)

    assert not product.is_displayed()


def test_main_page_gallery_next_and_back(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    product = page.elements(class_name="product_labeled")[0]

    page.element(class_name="carousel-arrow-right").click()

    time.sleep(1)

    assert not product.is_displayed()

    page.element(class_name="carousel-arrow-left").click()

    time.sleep(1)

    assert product.is_displayed()
