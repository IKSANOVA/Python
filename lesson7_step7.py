from selenium import webdriver
import time
import math


def calc():
    try:
        #return str(math.log(abs(12*math.sin(int(x)))))
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/get_attribute.html")
        time.sleep(3)
        x_element = browser.find_element_by_css_selector("#treasure")
        x = int(x_element.get_attribute("valuex"))
        print(x)
        #x = int(x_element.text)
        y = math.log(abs(12*math.sin(x)))

        answer_box = browser.find_element_by_css_selector('#answer')
        answer_box.send_keys(str(y))

        browser.find_element_by_css_selector('#robotCheckbox').click()
        browser.find_element_by_css_selector('#robotsRule').click()

        submit_box = browser.find_element_by_css_selector('body > div > form > div > div > button')
        submit_box.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла

if __name__ == "__main__":
    calc()