from shopNike.nike.element import BasePageElement
from shopNike.nike.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver



class MainPage(BasePage):


    def is_title_matches(self):
        return "Shoes" in self.driver.title


    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
    def search_item_by_keyword(self,item_name):
        element=self.driver.find_element(*MainPageLocators.SearchBar)
        element.send_keys(item_name)
        element.send_keys(Keys.RETURN)





class SearchResultsPage(BasePage):
    def is_element_present_by_css(self, value):
        try:
            self.driver.find_element_by_css_selector(value)
            return True
        except NoSuchElementException:
            return False

    def is_element_present_by_xpath(self, value):
        try:
            self.driver.find_element_by_xpath(value)
            return True
        except NoSuchElementException:
            return False

    def is_results_found(self):

        return "No results found." not in self.driver.page_source

    def click_element_by_xpath(self,value):

        self.driver.find_element(By.XPATH,value).click()

    def click_element_by_css(self, value):

        self.driver.find_element(By.CSS_SELECTOR, value).click()

    def type_into_by_xpath (self,xpath, value):
        self.driver.find_element(By.XPATH, xpath).send_keys(value)

    def type_into_by_css(self, css, value):
        self.driver.find_element(By.XPATH, css).send_keys(value)