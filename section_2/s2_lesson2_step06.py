from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #link = "https://suninjuly.github.io/selects1.html"
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)

    # Можно скрыть мешающий элемент
    footer = browser.find_element(By.TAG_NAME, 'footer')
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.ID, 'robotsRule')
    # Вариант со скролингом
    #browser.execute_script("window.scrollBy(0, 100);")
    option2.click()

    # Отправляем заполненную форму

    # browser.find_element_by_tag_name('body').send_keys(Keys.END)
    # или HOME если наверх

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Вариант со скролингом
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла