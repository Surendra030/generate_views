from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from decrypt import decrypt_json

import json
import os
import time
import random

# Set up Chrome options
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--headless") 
options.add_argument("--disable-notifications")  # Disable notifications
options.add_argument("--disable-blink-features=AutomationControlled")  # Disable the WebDriver flag

# Specify the path to your chromedriver
chromedriver_path = r"chromedriver"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

keypass = os.getenv('M_TOKEN')
file_name = 'encrypted_data.json'
data = decrypt_json(file_name, keypass)

try:
    random.shuffle(data)  # Shuffle data before processing
    print(f"Total URLs to process: {len(data)}")

    for index, url in enumerate(data):
        print(f"\nProcessing {index + 1}/{len(data)}: {url}")

        try:
            driver.get(url)
            print("Page loaded successfully.")
            time.sleep(2)

            body = driver.find_element("tag name", "body")  # Focus on the body
            print("Focused on page body.")

            for i in range(10):
                print(f"Scrolling iteration {i+1}/10")
                
                # Scroll right using SHIFT + >
                for j in range(4):
                    body.send_keys(Keys.SHIFT, ">")
                    time.sleep(1)
                    print(f"Scrolled right {j+1}/4")

                # Scroll using arrow keys
                for k in range(35):
                    ct = 'none'
                    try:
                        
                        current_time = driver.find_element(By.CSS_SELECTOR,".ytp-time-current")
                        ct = current_time.text
                    except Exception as e:
                        print("ct not found..")   
                    body.send_keys(Keys.ARROW_RIGHT)  # Simulate right arrow key
                    time.sleep(2)
                    print(f"{ct}_Moved right {k+1}/35")

                # Restart driver every iteration
                print("Restarting WebDriver...")
                driver.quit()
                time.sleep(15)
                
                service = Service(executable_path=chromedriver_path)
                driver = webdriver.Chrome(service=service, options=options)
                driver.get(url)
                time.sleep(2)
                body = driver.find_element("tag name", "body")  # Refocus on body
                print("WebDriver restarted and page reloaded.")

        except Exception as e:
            print(f"Error at index {index + 1}: {e}")

except Exception as e:
    print(f"Critical error encountered: {e}")

finally:
    driver.quit()
    print("WebDriver closed.")
