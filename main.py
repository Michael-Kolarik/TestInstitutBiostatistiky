from selenium import webdriver
from selenium.webdriver.common.by import By
import time
start = time.time() #pro zjištění doby testu
for index in range (1):#Pro automatické ověření ve dvou prohlížčích
    if index ==0:
        driver = webdriver.Chrome(executable_path = "C:\selenium browser drivers\chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="C:\selenium browser drivers\geckodriver.exe")
    driver.get("https://cs.laurie-project.com/login") #načtení stránky
    confirmation = driver.find_element_by_class_name("button primary success-button mr-10")
    confirmation.click() #potvrzení vyskakovacího okna
    login_field = driver.find_element_by_id("username-label")
    login_field.send_keys("TestovaciUcet")# Vyplnění uživatelského jména
    password_field = driver.find_element_by_id("pw-label")
    password_field.send_keys("Heslo123")#Vyplnění hesla
    login_button = driver.find_element_by_id("register-label")
    login_button.click()#Odeslání přihlášení
    if driver.current_url == "https://cs.laurie-project.com/home":
        out_link = driver.find_element_by_link_text("/logout")
        out_link.click()#Odhlášení
    else:
        print("Chyba přihlášení")#Chyba přihlášení
end = time.time()
print("Doba trvání testu v sekundách je", end-start)#Výpis doby testu