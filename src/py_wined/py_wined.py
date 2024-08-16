#%%
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

path_to_geckodriver = r"C:\Users\jfimb\Dropbox\py_wined\geckodriver\geckodriver.exe"

url = 'https://tastingbook.com'

service = Service(path_to_geckodriver)
driver = webdriver.Firefox(service=service)
driver.get(url)
# %%
# get div with class search-segment search-all

# inside search_div, get the input with class 'ui-autocomplete-input'
search_input = driver.find_element(By.CLASS_NAME, 'ui-autocomplete-input')
# search for chateau 
search_input.send_keys('chateau')
# wait 2 seconds 
driver.implicitly_wait(2)

#%%
# get all suggestions 
suggestions = driver.find_elements(By.CLASS_NAME, 'browse-label')
# %%
# href of each suggestion
first_suggestion = suggestions[0]
# click 
first_suggestion.click()
# %%
