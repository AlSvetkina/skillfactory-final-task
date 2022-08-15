from pages.labirint import MainPage


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
