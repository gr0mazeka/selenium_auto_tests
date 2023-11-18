from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#import math
import time

def calc(x,y):
  return str(int(x)+int(y))

try:
    #link = "https://suninjuly.github.io/selects1.html"
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#num1').text
    y = browser.find_element(By.CSS_SELECTOR, '#num2').text
    s = calc(x,y)

    # Код, который выбирает значение из списка
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_visible_text(s)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла