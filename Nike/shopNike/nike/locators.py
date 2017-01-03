from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SearchBar=(By.ID,'gnav-bar--search-input')
    GO_BUTTON = (By.ID, 'submit')
    PRODUCT_COUNT=(By.CSS_SELECTOR,'span.nsg-text--medium-light-grey')
    multiple_items_found='span.nsg-text--medium-light-grey'
    item_sold_out="//div[contains(text(),'Sold Out')]"
    size_elment="(//span[@class='js-selectBox-label'])[1]"
    shoe_size="//ul[@class='nsg-form--drop-down--option-container selectBox-options nsg-form--drop-down exp-pdp-size-dropdown exp-pdp-dropdown two-column-dropdown']/li[contains(text(),'{}')]"
    shoe_qty_element="//a[contains(text(),'QTY')]"
    shoe_qty="//li[@class='nsg-form--drop-down--option'and @rel='{}']"
    add_to_cart_button="//button[@id='buyingtools-add-to-cart-button']"
    check_out_page='https://secure-store.nike.com/us/checkout/html/cart.jsp'
    check_out_button="//input[@id='ch4_cartCheckoutBtn']"
    email="//input[@id='tunnelEmailInput']"
    password="//input[@name='tunnelPasswordInput']"
    member_checkout_btn="//input[@id='ch4_loginButton']"
    ccv_number="//input[@name='cvv' and @class='js-cvv cvv nsg-form--input validator-ignore is-invalid is-validated']"
    confirm_button="//button[text()='Confirm']"
    next_step_btn="//input[@value='Next Step']"

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass