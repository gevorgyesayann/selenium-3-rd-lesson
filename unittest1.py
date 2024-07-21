import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestUnit(unittest.TestCase):
    def test_for_lesson1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your first name"]')
        input1.send_keys('g')
        input2 = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your last name"]')
        input2.send_keys('a')
        input3 = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your email"]')
        input3.send_keys('s')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)
    
    def test_for_lesson2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your first name"]')
        input1.send_keys('g')
        input2 = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your last name"]')
        input2.send_keys('a')
        input3 = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your email"]')
        input3.send_keys('s')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)
        time.sleep(10)

if __name__=="__main__":
    unittest.main()