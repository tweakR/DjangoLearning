import time
import unittest

from django.test.testcases import LiveServerTestCase
from pip._vendor.retrying import MAX_WAIT
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\chromedriver/chromedriver")
        self.addCleanup(self.driver.quit)

    def tearDown(self):
        self.driver.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.driver.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get(self.live_server_url)
        self.assertIn('To-Do', self.driver.title)
        header_text = self.driver.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)

        input_box = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        input_box = self.driver.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')


if __name__ == '__main__':
    unittest.main(verbosity=2)
