#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time



# In[8]:


class souper(object):
    
    def __init__(self):
        None
           
    def get_soup(self, URL, click=False, element=None):
        # Setting options to run headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--window-size=2880,1800')

        # Installing temporary Chrome webdriver
        driver = webdriver.Chrome(ChromeDriverManager().install(),
                                 options=chrome_options)

        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        # Trying to get URL and refreshing in case of TimeoutException
        try:
            driver.get(URL)
            wait = WebDriverWait(driver, 10)
        except TimeoutException as ex:
            driver.navigate().refresh()

        # Entering if get_soups needs 
        if click:

            # In case of being banned, tries again
            if len(driver.find_elements_by_css_selector("[name=ROBOTS]")) > 0:
                try:
                    driver.get(URL)
                    wait = WebDriverWait(driver, 10)
                except TimeoutException as ex:
                    driver.navigate().refresh()

            # Collecting path and clicking
            tab_click = driver.find_element_by_xpath(str(element))
            tab_click.click()

            # Sleeps for a while to get te refreshed code
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source)
            driver.close()

        # Second case if of not needing clicking
        else:
            if len(driver.find_elements_by_css_selector("[name=ROBOTS]")) > 0:
                try:
                    driver.get(URL)
                    wait = WebDriverWait(driver, 10)
                except TimeoutException as ex:
                    webDriver.navigate().refresh()
            soup = BeautifulSoup(driver.page_source,'html.parser')
            driver.close()

        return soup






