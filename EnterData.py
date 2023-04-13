from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')

    def test_search(self):
        driver = self.driver
        driver.get('http://www.google.com')
        self.assertIn('Google', driver.title)
        elemento = driver.find_element(By.NAME, 'q')
        elemento.send_keys('Hola Mundo!')
        elemento.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No Found it:" not in driver.page_source

    def teamDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()