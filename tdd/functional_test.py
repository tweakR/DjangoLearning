import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/viacheslav/chromedriver/chromedriver")
        self.addCleanup(self.driver.quit)

    def test_page_title(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('Django', self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
