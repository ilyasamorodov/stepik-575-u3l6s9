# import time


def test_product_page_has_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # time.sleep(10)
    basket_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    # I use find_elements_ instead of find_element because it returns an array
    # and helps to avoid NoSuchElementException in this case
    assert len(basket_button) > 0, "Add to basket button not found"
