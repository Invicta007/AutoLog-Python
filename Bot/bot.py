# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def startBot(username, password, url):
    driver_path = r"D:\AutoLog\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keeps browser open after script

    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    # Wait for elements to load
    driver.implicitly_wait(5)

    # Fix: Ensure correct element selectors and check if elements exist
    try:
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "loginBtn").click()
        driver.find_element(By.ID, "email").send_keys(username)
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.ID, "u_0_5_gO").click()
    except Exception as e:
        print("Error during login:", e)

# --- Driver code ---
username = "9656427794"
password = "Gocct*123"
url = "https://www.facebook.com/"
startBot(username, password, url)
