from pages.labirint import MainPage

def test_main_page_book_details(web_browser):
    """ Make sure that link to novelty works on big screen """
    page = MainPage(web_browser, url='/')

    book = page.elements(class_name="product")[0]
    id = book.get_attribute("data-product-id")

    book.click()

    assert page.get_current_url() == f'{page._base_url}/books/{id}/'

    book = page.elements(class_name="product")[0]
    assert id == book.get_attribute("data-product-id")
