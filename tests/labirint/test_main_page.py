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

    assert 'Букварь' in suggestions.get_text()[0]


def test_check_search_cancelation(web_browser):
    page = MainPage(web_browser, url='/')

    page.search.set_value(",erdfhm")
    cancel_btn = page.element(class_name="b-header-b-search-e-clear-btn-wrap")
    cancel_btn.click()
    time.sleep(1)

    suggestions_block = page.element(id="autohelp_rows")

    assert suggestions_block.is_visible()


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


#  def test_check_top_header_club(web_browser):
    #  """ Make sure that link to office page works """

    #  page = MainPage(web_browser, url='/')

    #  top_bar_element = 6
    #  top_header = page.elements(class_name="b-header-b-menu-e-text")
    #  href = top_header[top_bar_element].get_attribute('href')
    #  top_header[top_bar_element].click()
    #  time.sleep(1)

    #  assert page.get_current_url() == href
