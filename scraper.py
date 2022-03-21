# from selenium.common.exceptions import NoSuchElementException
# import time, uuid, os, json, boto3, tempfile, datetime
# from config import aws_creds
# import pandas as pd
# from sqlalchemy import create_engine
# from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ScraperTemplate:
    def __init__(self, url:str, options=None):
        self.url = url
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        PATH = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(PATH, options=options)

        self.all_url = []
    
    def finding_links(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href]")))
            loop = self.driver.find_elements(By. XPATH, "//a[@href]")
            for links in loop:
                self.all_url.append(links.get_attribute("href"))
        except:
            print("No links found. Website might not have loaded correctly. Try again.")
        self.all_url.sort()
        print(f"Successfully created list of all url's: {len(self.all_url)}")
        return self.all_url

    def validate_links(self):
        pass

    def action_or_looping(self):
        pass