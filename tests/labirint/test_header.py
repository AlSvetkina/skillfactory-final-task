from pages.labirint import MainPage


def test_header_click_logo(web_browser):
    """ Make sure that main logo always leads to main page. """

    page = MainPage(web_browser, url='/')

    book = page.elements(class_name="product")[0]
    id = book.get_attribute("data-product-id")

    book.click()

    assert page.get_current_url() == f'{page._base_url}/books/{id}/'

    page.elements(class_name="b-header-b-logo-e-logo-wrap")[0].click()

    assert page.get_current_url() == f'{page._base_url}/'
