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

keypass = 'myApp101!'
file_name = 'encrypted_data.json'
data = decrypt_json(file_name,keypass)

try:
     while(True):   
        for index,url in enumerate(data):
            try:
                    
                if index%20==0:
                    driver.quit()
                    time.sleep(15)
                    service = Service(executable_path=chromedriver_path)
                    driver = webdriver.Chrome(service=service, options=options)
                    

                driver.get(url)
                time.sleep(2)
                body = driver.find_element("tag name", "body")  # Focus on the body

                # Wait for the page to load
                for i in range(4):
                    body.send_keys(Keys.SHIFT, ">")
                    time.sleep(1)
                    
                for i in range(35):
                        
                    # Send the right arrow key or 'L' key
                    body.send_keys(Keys.ARROW_RIGHT)  # Simulate right arrow key
                    time.sleep(2)
                time.sleep(10)
                
            except Exception as e:
                print("Error 59 :",e)
            
except Exception as e:
    print("Error 63 ",e)