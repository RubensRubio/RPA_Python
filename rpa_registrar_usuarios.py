import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usuarios = pd.read_excel('usuarios.xlsx')

driver = webdriver.Chrome()
driver.get('https://cognitivetesting.online')

wait = WebDriverWait(driver, 20)

# =========================
# LOGIN
# =========================

email_login = "rrubio@cryoinfra.com.mx"
password_login = "Huawei.3091"

wait.until(
    EC.visibility_of_element_located((By.ID, "exampleInputEmail1"))
).send_keys(email_login)

wait.until(
    EC.visibility_of_element_located((By.ID, "exampleInputPassword1"))
).send_keys(password_login)

btn_login = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Login']]"))
)
btn_login.click()

# Esperar a que cargue la página después del login
time.sleep(3)

# =========================
# SELECCIONAR APP_Gastos
# =========================

card_app = wait.until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[contains(text(), 'APP_Gastos')]/ancestor::div[contains(@class,'ant-card')]"))
)

btn_menu = card_app.find_element(By.XPATH,
                                 ".//*[name()='svg' and contains(@class, 'MuiSvgIcon-root')]")
btn_menu.click()

btn_manage_permissions = wait.until(
    EC.element_to_be_clickable((By.XPATH,
                                "//a[contains(text(),'Manage permissions')]"))
)

btn_manage_permissions.click()

for index, row in usuarios.iterrows():
    email = row['Email']

    print(f"Registrando usuario: {email}")

    btn_add = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Add']"))
    )
    driver.execute_script("arguments[0].click();", btn_add)

    fila_add = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr[@mode='add']"))
    )

    input_mail = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//tr[@mode='add']//input[@aria-label='Mail']"))
    )
    # input_mail = fila_add.find_element(By.XPATH, ".//input[@aria-label='Mail']")
    # input_mail.click()
    # input_mail.send_keys(email)
    driver.execute_script("arguments[0].focus();", input_mail)
    driver.execute_script("arguments[0].value = arguments[1];", input_mail, email)
    driver.execute_script("""
    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, input_mail)

    chk_editor_visual = wait.until(
        EC.presence_of_element_located(
                (By.XPATH, 
                 "//tr[@mode='add']/td[4]//span[contains(@class,'MuiCheckbox-root')]"))
        )
    
    driver.execute_script("arguments[0].click();", chk_editor_visual)
    time.sleep(1)

    btn_save = fila_add.find_element(By.XPATH, ".//button[@title='Save']")
    # driver.execute_script("arguments[0].click();", btn_save)
    # btn_save.click()

    # wait.until(
    #     EC.invisibility_of_element_located((By.XPATH, "//tr[@mode='add']"))
    # )

    time.sleep(3)
    print(f"Usuario {email} registrado con permisos de editor.")

print("Todos los usuarios han sido registrados.")
driver.quit()
