from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math
import time

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'empty_file.txt')


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.CSS_SELECTOR,
                                    '.form-control[name="firstname"]')
    input2 = browser.find_element(By.CSS_SELECTOR,
                                    '.form-control[name="lastname"]')
    input3 = browser.find_element(By.CSS_SELECTOR,
                                    '.form-control[name="email"]')
    element = browser.find_element(By.ID, 'file')
    input1.send_keys('Ivan')
    input2.send_keys('Petrov')
    input3.send_keys('petr@v.iv')
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла