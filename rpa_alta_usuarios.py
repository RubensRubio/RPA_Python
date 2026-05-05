import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usuarios = pd.read_excel('usuarios.xlsx')

driver = webdriver.Chrome()
driver.get('https://cognitivetesting.online')

signup_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sign up')]"))
)
signup_link.click()

time.sleep(3)

for index, row in usuarios.iterrows():
    nombre = row['Nombre']
    apellidos = row['Apellidos']
    email = row['Email']
    password = row['Password']
    
    driver.find_element(By.ID, 'exampleInputName').clear()
    driver.find_element(By.ID, 'exampleInputName').send_keys(nombre)
    
    driver.find_element(By.ID, 'exampleInputLastName').clear()    
    driver.find_element(By.ID, 'exampleInputLastName').send_keys(apellidos)
    
    driver.find_element(By.ID, 'exampleInputEmail1').clear()    
    driver.find_element(By.ID, 'exampleInputEmail1').send_keys(email)

    driver.find_element(By.ID, 'exampleInputPassword1').clear()    
    driver.find_element(By.ID, 'exampleInputPassword1').send_keys(password)
    
    driver.find_element(By.ID, 'exampleInputPassword2').clear()    
    driver.find_element(By.ID, 'exampleInputPassword2').send_keys(password)
    
    # driver.find_element(By.XPATH, "//button[.//span[text()='Sign up']]").click()
    print(f"Usuario {nombre} {apellidos} - {email} | {password} registrado.")
    time.sleep(2)
    
print("Todos los usuarios han sido registrados.")
driver.quit()