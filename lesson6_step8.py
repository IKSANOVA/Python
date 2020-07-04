from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block>div.form-group.first_class>input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block>div.form-group.second_class>input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block>div.form-group.third_class>input.form-control.third")
    input3.send_keys("test@test.ru")
    button = browser.find_element_by_xpath("//button[(text())='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла