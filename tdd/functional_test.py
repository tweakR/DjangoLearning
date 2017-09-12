import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\geckodriver\chromedriver.exe")
        self.addCleanup(self.driver.quit)
        self.driver.implicitly_wait(3)

    def test_page_title(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('To-Do', self.driver.title)
        self.fail('Finish Test')


if __name__ == '__main__':
    unittest.main(verbosity=2)
