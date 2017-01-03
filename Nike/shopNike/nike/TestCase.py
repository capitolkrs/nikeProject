import unittest
from selenium import webdriver
from shopNike.nike import page
from selenium.webdriver.common.by import By
from shopNike.nike.locators import MainPageLocators
from shopNike.nike.property import properties

import time

class nikeSearchPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/capitalterefe/Documents/DevTools/chromedriver')
        url='http://www.nike.com/us/en_us/c/men'
        self.driver.get(url)

    def test_search_items(self):

        # item_name = 'JORDAN'
        main_page = page.MainPage(self.driver)
        search_results_page = page.SearchResultsPage(self.driver)

        assert main_page.is_title_matches(), "nike.com title doesn't match."

        main_page.search_item_by_keyword(properties.item_name)
        time.sleep(5)
        # check if multiple items are displayed after search
        multiple_items_found=search_results_page.is_element_present_by_css(MainPageLocators.multiple_items_found)
        item_sold_out=search_results_page.is_element_present_by_xpath(MainPageLocators.item_sold_out)
        size_element=MainPageLocators.size_elment
        shoe_qty_element=MainPageLocators.shoe_qty_element
        shoe_qty=MainPageLocators.shoe_qty.format(properties.qty)
        shoe_size=MainPageLocators.shoe_size.format(properties.size)
        add_to_cart=MainPageLocators.add_to_cart_button
        checkout_page=MainPageLocators.check_out_page
        checkout_button=MainPageLocators.check_out_button
        email=MainPageLocators.email
        password=MainPageLocators.password
        member_checkout_btn=MainPageLocators.member_checkout_btn
        cvv_number=MainPageLocators.ccv_number
        confirm_button=MainPageLocators.confirm_button
        next_step_btn=MainPageLocators.next_step_btn
        print(multiple_items_found ,item_sold_out)

        #if single item found then proceed to checkout
        if not multiple_items_found:
            # check if it's not sold out, if not proceed in selecting size and quantity
            if not item_sold_out:
                search_results_page.click_element_by_xpath(size_element)
                search_results_page.click_element_by_xpath(shoe_size)
                search_results_page.click_element_by_xpath(shoe_qty_element)
                search_results_page.click_element_by_xpath(shoe_qty)
                search_results_page.click_element_by_xpath(add_to_cart)
                time.sleep(5)
                self.driver.get(checkout_page)
                time.sleep(5)
                search_results_page.click_element_by_xpath(checkout_button)
                time.sleep(5)
                search_results_page.type_into_by_xpath(email,properties.email)
                search_results_page.type_into_by_xpath(password, properties.password)
                search_results_page.click_element_by_xpath(member_checkout_btn)
                time.sleep(30)
                test1= self.driver.find_element_by_css_selector("input#cvv-usercc38429787").is_displayed()
                self.driver.find_element(By.ID,'cvv-usercc38429787').send_keys("hello")
                test=search_results_page.is_element_present_by_xpath(cvv_number)
                print(test)
                print(test1)

                search_results_page.click_element_by_xpath(cvv_number)
                search_results_page.type_into_by_xpath(cvv_number,properties.cvv)
                time.sleep(10)
                search_results_page.click_element_by_xpath(confirm_button)
                search_results_page.click_element_by_xpath(next_step_btn)

        assert search_results_page.is_results_found(), "No results found."
        time.sleep(10)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()