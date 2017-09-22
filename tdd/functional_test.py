import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\chromedriver/chromedriver")
        self.addCleanup(self.driver.quit)

    def tearDown(self):
        self.driver.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_page_title(self):
        self.driver.get('http://localhost:8000')
        header_text = self.driver.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)
        input_box = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        input_box = self.driver.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock to make a fly')


if __name__ == '__main__':
    unittest.main(verbosity=2)
