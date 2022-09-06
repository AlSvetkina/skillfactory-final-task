from pages.labirint import MainPage


def test_compare_book_open_compare_menu(web_browser):
    """ Make sure that we can open compare menu on a book. """

    page = MainPage(web_browser, url='/')
    page.elements(class_name="icon-compare")[0].click()

    compare = page.elements(class_name="js-card-block-actions-compare")[0]
    compare.click()
    assert compare.is_displayed()


def test_compare_add_book_to_compare_list_1(web_browser):
    """ Make sure that we can add a book to the compare list. """

    page = MainPage(web_browser, url='/')

    page.elements(class_name="icon-compare")[0].click()

    compare = page.elements(class_name="js-card-block-actions-compare")[0]
    compare.click()

    assert compare.text == "Перейти к сравнению"


def test_compare_add_book_to_compare_list_and_close_menu(web_browser):
    """ Make sure that we can add a book to the compare list and close menu."""

    page = MainPage(web_browser, url='/')
    page.elements(class_name="icon-compare")[0].click()

    compare = page.elements(class_name="js-card-block-actions-compare")[0]
    compare.click()

    page.send_escape()

    assert not compare.is_displayed()


def test_compare_add_two_books_and_compare(web_browser):
    """ Make sure that we can add two books to the compare list. """

    page = MainPage(web_browser, url='/')
    web_browser.execute_script("window.scrollBy(0,500)")

    page.elements(class_name="icon-compare")[0].click()

    compare_1 = page.elements(class_name="icon-compare")[0]
    book_title_1 = compare_1.get_attribute("data-title")

    compare_2 = page.elements(class_name="icon-compare")[1]
    book_title_2 = compare_2.get_attribute("data-title")

    assert book_title_1 != book_title_2

    compare_1.click()
    compare_1 = page.elements(class_name="js-card-block-actions-compare")[0]
    compare_1.click()
    page.send_escape()

    compare_2.click()
    compare_2 = page.elements(class_name="js-card-block-actions-compare")[0]
    compare_2.click()
    compare_2.click()

    assert page.wait_for_url('compare/')

    assert page.elements(class_name="item-name__href").count() == 2


def test_compare_add_two_books_and_compare_and_cancel(web_browser):
    """ Make sure that we can clear compare list. """

    page = MainPage(web_browser, url='/')
    web_browser.execute_script("window.scrollBy(0,500)")

    page.elements(class_name="icon-compare")[0].click()

    compare_1 = page.elements(class_name="icon-compare")[0]
    compare_1.click()
    compare_1 = page.elements(class_name="js-card-block-actions-compare")[0]
    compare_1.click()
    page.send_escape()

    compare_2 = page.elements(class_name="icon-compare")[1]
    compare_2.click()
    compare_2 = page.elements(class_name="js-card-block-actions-compare")[0]
    compare_2.click()
    compare_2.click()

    assert page.wait_for_url('compare/')

    page.elements(class_name="compare-delete-list__text")[0].click()

    assert page.elements(class_name="item-name__href").count() == 0
