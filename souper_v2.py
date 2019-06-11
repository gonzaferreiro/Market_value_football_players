#!/usr/bin/env python
# coding: utf-8

# In[26]:


from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


# In[28]:


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
        
        # Setting waiting time in case of not finding elements
        driver.implicitly_wait(30)
        
        # Creating empy variable soup in case of failing
        soup = ""
        
        # Trying to get URL and refreshing in case of TimeoutException
        try:
            driver.get(URL)
        except TimeoutException as ex:
            driver.refresh()
            try:
                driver.get(URL)
            except TimeoutException as ex:
                print('TimeoutException insisted at first')
                pass

        # Entering if get_soups needs click 
        if click:

            # In case of being banned, tries again
            if len(driver.find_elements_by_css_selector("[name=ROBOTS]")) > 0:
                try:
                    driver.get(URL)
                except TimeoutException as ex:
                    driver.refresh()
                    try:
                        driver.get(URL)
                    except TimeoutException as ex:
                        print('TimeoutException insisted when clicking')
                        pass

            # Collecting path and clicking
            wait = WebDriverWait(driver, 10)
            tab_click = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            #tab_click = waiter.find_element_by_xpath(element)
            tab_click.click()

            # Sleeps for a while to get te refreshed code
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source,'html.parser')
            driver.close()

        # Second case if of not needing clicking
        else:
            if len(driver.find_elements_by_css_selector("[name=ROBOTS]")) > 0:
                try:
                    driver.get(URL)
                except TimeoutException as ex:
                    driver.refresh()
                    try:
                        driver.get(URL)
                    except TimeoutException as ex:
                        print('TimeoutException at second')
                        pass
                    
            soup = BeautifulSoup(driver.page_source,'html.parser')
            driver.close()
        
        return soup


# In[ ]:




