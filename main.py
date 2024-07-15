from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import getpass

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])  
options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com')

email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
email.send_keys(input("Login: "))

senha = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
senha.send_keys(getpass.getpass("Password: "))

entrar_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
entrar_button.click()   


input()

driver.get("https://www.facebook.com/groups/434953423375127")

images = [
    "foto1.jpg",
    "foto2.jpg",
    "foto3.jpg",
    "foto4.jpg",
    "foto5.jpg",
    "foto6.jpg",
]

value = 1

for image in images:
    try: 
        sleep(0.5)
        xpath_input = f'(//input[@type="file"])[{value}]'
        input_arquivo = driver.find_element(By.XPATH, xpath_input)
        input_arquivo.send_keys(image)
        value = 3
    except Exception as e:
        print(f"Erro ao enviar arquivo: {e}")

input()
driver.quit()
