import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/viacheslav/chromedriver/chromedriver")
        self.addCleanup(self.driver.quit)

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        self.driver.get('http://localhost:8000')
        header_text = self.driver.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)

        input_box = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('place_holder'), 'Enter a to-do item')
        input_box.send_keys('Buy peacock feathers')

        input_box.send_keys(Keys.ENTER)

        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))


if __name__ == '__main__':
    unittest.main(verbosity=2)
