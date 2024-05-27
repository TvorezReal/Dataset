from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()

# URL страницы
url = 'https://divan.ru/category/pramye-divany'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@class='ui-LD-ZU KIkOH']")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()