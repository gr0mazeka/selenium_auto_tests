import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = " http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get(link)

        input1 = self.browser.find_element(
                                        By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys("Ivan")
        input3 = self.browser.find_element(
                                        By.CSS_SELECTOR, '.first_block .third')
        input3.send_keys("pet@iv.an")
        input2 = self.browser.find_element(
                                        By.CSS_SELECTOR, '.first_block .second')
        input2.send_keys("Petrov")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text)

        time.sleep(1)
        self.browser.quit()

    def test_reg2(self):
        link = " http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get(link)

        input1 = self.browser.find_element(
                                        By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys("Ivan")
        input3 = self.browser.find_element(
                                        By.CSS_SELECTOR, '.first_block .third')
        input3.send_keys("pet@iv.an")
        input2 = self.browser.find_element(
                                        By.CSS_SELECTOR, '.first_block .second')
        input2.send_keys("Petrov")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text)

        time.sleep(1)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()