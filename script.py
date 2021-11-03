import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://arithmetic.zetamac.com")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, 'form.game-options select[name="duration"]').click()
driver.find_element(By.CSS_SELECTOR, 'form.game-options select[name="duration"] option[value="30"]').click()
driver.find_element(By.CSS_SELECTOR, 'form.game-options input[value="Start"]').click()

problem = driver.find_element(By.CSS_SELECTOR, '#game div.start span.problem')
answer = driver.find_element(By.CSS_SELECTOR, '#game div.start input.answer')
while text := problem.text:
    x, operation, y = text.split()
    x = int(x)
    y = int(y)
    if operation == "+": z = x + y
    elif operation == "–": z = x - y
    elif operation == "×": z = x * y
    elif operation == "÷": z = x // y
    answer.send_keys(str(z))

time.sleep(2)
driver.close()
