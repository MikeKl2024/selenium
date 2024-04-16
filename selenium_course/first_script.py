# import time

# from selenium import webdriver

# from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()

# time.sleep(5)

# driver.get("https://www.google.com/?hl=ru")
           
# time.sleep(7)


# textarea=driver.find_element(By.CSS_SELECTOR,".gLFyf")

# textarea.send_keys("get()")

# time.sleep(5)

# submit_button=driver.find_element(By.CSS_SELECTOR, ".gNO89b")

# submit_button=driver.find_element(By.CSS_SELECTOR, ".RNmpXc")

# submit_button.click()

# time.sleep(5)

# driver.quit()


# from selenium import webdriver


# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# import time


# link = "http://suninjuly.github.io/simple_form_find_task.html"

# try:
   

#     browser = webdriver.Chrome()
#     browser.get(link)
#     input_1 = browser.find_element(By.NAME, "first_name")
#     input_1.send_keys('Bob')
#     input_2 = browser.find_element(By.NAME, "last_name")
#     input_2.send_keys('Dragon')
#     input_3 = browser.find_element(By.CLASS_NAME, "city")
#     input_3.send_keys('Vegas')
#     # input_3_1 = browser.find_element(By.CSS_SELECTOR, ".city")
#     # input_3_1.send_keys('Spichak')
#     input_4 = browser.find_element(By.ID, "country")
#     input_4.send_keys('Angy')
#     # input_4_1 = browser.find_element(By.CSS_SELECTOR, "#country")
#     # input_4_1 .send_keys('Spichak')
#     button_5 = browser.find_element(By.ID, "submit_button")
#     button_5.click()

    
 
# finally:
#     time.sleep(12)
#     #закрывает браузер после всех манипуляций даже если была ошибка
#     browser.quit()
   

# from selenium import webdriver

# from selenium.webdriver.common.by import By

# import time

# link = "https://www.degreesymbol.net/"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
#     link.click()

# finally:
#     time.sleep(12)
    
#     browser.quit()
   



#Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver

# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By

# import time
# import math



# link = "http://suninjuly.github.io/find_link_text"


# a= str(math.ceil(math.pow(math.pi, math.e)*10000))

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, a)
#     link.click()
#     input_1 = browser.find_element(By.NAME, "first_name")
#     input_1.send_keys('Erik')
#     input_2 = browser.find_element(By.NAME, "last_name")
#     input_2.send_keys('Spichak')
#     input_3 = browser.find_element(By.CLASS_NAME, "city")
#     input_3.send_keys('Spichak')
#     # input_3_1 = browser.find_element(By.CSS_SELECTOR, ".city")
#     # input_3_1.send_keys('Spichak')
#     input_4 = browser.find_element(By.ID, "country")
#     input_4.send_keys('Spichak')
#     # input_4_1 = browser.find_element(By.CSS_SELECTOR, "#country")
#     # input_4_1 .send_keys('Spichak')
#     button_5 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]' )
#     button_5.click()
#     # button_5_1 = browser.find_element(By.CSS_SELECTOR, "#submit_button")
#     # button_5_1.click()




# finally:
#     time.sleep(12)
#     #закрывает браузер после всех манипуляций даже если была ошибка
#     browser.quit()


# from selenium import webdriver


# from selenium.webdriver.common.by import By

# import time
# import math



# link = "https://easysmarthub.ru/contact/"


# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     input_1 = browser.find_element(By.NAME,"your-name")
#     input_1.send_keys("Михаил")
#     input_2 = browser.find_element(By.NAME,"your-email")
#     input_2.send_keys("mikhail.@kleschenko.com")
#     input_3 = browser.find_element(By.NAME,"your-subject")
#     input_3.send_keys("Курс") 
#     input_4 = browser.find_element(By.NAME, "your-message")
#     input_4.send_keys("Тест Курс")
#     button_5 = browser.find_element(By.CSS_SELECTOR,'[type="checkbox"]')
#     button_5.click()
#     button_6 = browser.find_element(By.CSS_SELECTOR,'[type="submit"]' )
#     button_6.click()
# finally:
#     time.sleep(12)
#     browser.quit()


# from selenium import webdriver


# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# import time



# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/huge_form.html")


# elements = browser.find_elements(By.TAG_NAME, 'input')
# for i in elements:
#         i.send_keys("Привет")
# buton = browser.find_element(By.TAG_NAME,'button')
# buton.click()


# browser.quit()

# time.sleep(12)





# from selenium import webdriver


# импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# import time



# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/registration1.html")


# elements = browser.find_elements(By.TAG_NAME, 'input')
# for i in elements:
#          i.send_keys("Привет")
# buton = browser.find_element(By.TAG_NAME,'button')

# time.sleep(12)
# buton.click()


# browser.quit()






# from selenium import webdriver




# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# import time


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/registration1.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for i in elements:
#         if i.get_attribute('required'):
#             i.send_keys("ghbdtn")
#     buton = browser.find_element(By.TAG_NAME,'button')
#     buton.click()




#     #находим элемент содержащитй текст
#     welcome_text = browser.find_element(By.TAG_NAME, "h1")
#     #запишем текст из h1 в переменную
#     welcome = welcome_text.text
   
#     #с помощью assert проверяю, что ожидаемый текст совпадает с текстом на странице
#     assert "Congratulations! You have successfully registered!" == welcome
   
# finally:
#     time.sleep(5)
#     browser.quit()




#Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver




# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# import time


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/registration2.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for i in elements:
#         if i.get_attribute('required'):
#             i.send_keys("ghbdtn")
#     buton = browser.find_element(By.TAG_NAME,'button')
#     buton.click()


#     time.sleep(1)




#     #находим элемент содержащитй текст
#     welcome_text = browser.find_element(By.TAG_NAME, "h1")
#     #запишем текст из h1 в переменную
#     welcome = welcome_text.text
   
#     #с помощью assert проверяю, что ожидаемый текст совпадает с текстом на странице
#     assert "Congratulations! You have successfully registered!" == welcome
   
# finally:
#     time.sleep(5)
#     browser.quit()

# from selenium import webdriver

 
# from selenium.webdriver.common.by import By


# import time
# import math



# browser = webdriver.Chrome()
# browser.get("https://suninjuly.github.io/get_attribute.html")

# 'https://suninjuly.github.io/get attribute.htn]'

# def calc(x):
# return math.log(abs(12*math.Stntanc(x))))

# try:

# browser = webdriver. Chrome
# browser =get(link)
#image = browser,find_element(By.ID, 'treasure') image_check - image-get_attribute('valuex')
# x - image_check
# y = calc(x)
# time.sleep(1)
# element = browser. find_element (By.ID, 'answer*)
# element.send _keys (Y)
# elementchek = browser. find_ element(By.ID, "robotCheckbox*) elementchek.click()
# elementchek1 = browser. find_element (By.ID, 'robotsRule')
# elementchek1. click()
# buttons
# - browser. find_element (By.CSS_SELECTOR, *.btn-default')
# DUE TONI
# click()
# finally:
# tise-sleep(10) browser quit()



# from selenium import webdriver
 
# from selenium.webdriver.common.by import By

# import time

# from selenium.webdriver.support.ui import Select

# browser = webdriver.Chrome()
# browser.get("https://www.uefa.com/euro2024/ticketing/")

# time.sleep(10)
# buton = browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/div[2]/header/div/div[1]/div/div/pk-button[2]")
# buton.click()
# sum= browser.find_elements (By.CLASS_NAME,"nowrap")
# num1=browser.find_elements (By.ID,id="num1")
# num2=browser.find_elements (By.ID,id="num2")



#Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver




# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import Select


# import time


# try:
#     browser = webdriver.Chrome()
#     browser.get("https://suninjuly.github.io/selects1.html")


#     span_element_1 = browser.find_element(By.ID, "num1")
#     text_from_span_1 = span_element_1.text
#     number_from_span_1 = int(text_from_span_1)
#     print(number_from_span_1)
#     span_element_2 = browser.find_element(By.ID, "num2")
#     text_from_span_2 = span_element_2.text
#     number_from_span_2 = int(text_from_span_2)
#     print(number_from_span_2)
#     span_sums = number_from_span_1 + number_from_span_2
#     print(span_sums)
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(span_sums))
#     btn = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     btn.click()


   


   
   
# finally:
#     time.sleep(5)
#     browser.quit()





from selenium import webdriver
 
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.ui import Select
import os 


# browser = webdriver.Chrome()
# browser.get("https://suninjuly.github.io/file_input.html")

# input_1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
# input_1.send_keys('Mik')
# input_2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"')
# input_2.send_keys('Kle')
# input_3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
# input_3.send_keys('mob')
# time.sleep(5)
# cur_dir = os.path.abspath(os.path.dirname(__file__))


# file_path = os.path.join(cur_dir, 'file.txt')
# element = browser.find_element(By.CSS_SELECTOR,'[type="file"]')
# element.send_keys(file_path)


# btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
# btn.click()


# time.sleep(5)

# def calc()
# return math.log(abs(12*math.Stntanc(x))))     

# try:
#     browser = webdriver.Chrome()
#     browser.get("https://suninjuly.github.io/alert_accept.html")
#     buton = browser.find_element(By.TAG_NAME,'button')
#     buton.click()



#     confirm = browser.switch_to.alert
#     confirm.accept() # принять
#     confirm.dismiss() #отклонить
# finally:
#     time.sleep(5)
#     browser.quit()



# from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import Select


# import time
# import math

# try:
#     browser = webdriver.Chrome()
#     browser.get("https://suninjuly.github.io/alert_accept.html")
#     def calc(x):
#         return str(math.log(abs(12*math.sin(x))))
   
#     btn =browser.find_element(By.TAG_NAME, 'button')
#     btn.click()
#     confim = browser.switch_to.alert
#     confim.accept()
#     math_element = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]')
#     x = int(math_element.text)
#     input_form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
#     input_form.send_keys(calc(x))
#     button = browser.find_element(By.TAG_NAME, 'button')
#     button.click()
     
# finally:
#     time.sleep(20)
#     browser.quit()


#Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver




# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import Select


# import time
# import math
# import os


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/redirect_accept.html")
#     btn = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
#     btn.click()
#     window_page = browser.window_handles[1]
#     browser.switch_to.window(window_page)
#     def calc(x):
#         return str(math.log(abs(12*math.sin(x))))
#     math_element = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]')
#     x = int(math_element.text)
#     input_form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
#     input_form.send_keys(calc(x))
#     button = browser.find_element(By.TAG_NAME, 'button')
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()






# from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import Select


# import time
# import math
# import os


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/wait1.html")
#     time.sleep(5)
#     btn = browser.find_element(By.ID,"verify")
#     btn.click()
#     massage=browser.find_element(By.ID,"verify_message")
#     assert "successful" in massage.text



# finally:
#      time.sleep(5)







#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


import time
import math
import os


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
    btn = browser.find_element(By.ID, 'book')
    btn.click()
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))
    x = browser.find_element(By.ID,'input_value')
    x = int(x.text)
    input_block = browser.find_element(By.ID,'answer')
    input_block.send_keys(str(calc(x)))
    btn_2 = browser.find_element(By.ID,'solve')
    btn_2.click()




finally:
    time.sleep(10)
    browser.quit()











