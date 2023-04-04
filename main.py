from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import requests


# ---------------------------REQUIREMENTS-------------------------------------

FOLDER = ""
COMIC_URL = ""

# ------------------------------------------------------------------------------

os.makedirs(FOLDER, exist_ok=True)
service = Service("C:\\Users\Dell\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(COMIC_URL)
driver.maximize_window()

chapter = driver.find_elements(By.CSS_SELECTOR, ".main div a")
urls = {}

for x in chapter:
    url = x.get_attribute('href')
    name = x.text
    if "user" not in url:
        urls[name] = url

    print(urls)

for key, value in urls.items():

    SUB_FOLDER = f"{FOLDER}\{key}"
    os.makedirs(SUB_FOLDER, exist_ok=True)
    driver.get(value)
    driver.maximize_window()

    file = 0
    image = driver.find_elements(By.CLASS_NAME, "page-img")

    for x in image:
        url = x.get_attribute("src")
        file += 1
        filename = f'{file}.webp'
        print('url:', url)
        print('filename:', filename)
        print('-----')
        full_path = os.path.join(SUB_FOLDER, filename)
        print(full_path)

        response = requests.get(url)
        data = response.content
        with open(full_path, "wb") as fh:
            fh.write(response.content)