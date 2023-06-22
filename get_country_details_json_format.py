
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import json

baseUrl="https://www.scrapethissite.com/pages/simple/"
website_title = "Countries of the World: A Simple Example | Scrape This Site | A public sandbox for learning web scraping"
country_name_selector = ".country-name"
country_capital_name_selector = ".country-capital"
country_population_selector = ".country-population"

def browserOpen():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(baseUrl)
    driver.implicitly_wait(5)
    return driver

# Open the Browser with the URL
driver = browserOpen()
# verify the Web page load properly
assert website_title in driver.title
country_name_list = driver.find_elements(By.CSS_SELECTOR,country_name_selector)
capital_name_list = driver.find_elements(By.CSS_SELECTOR,country_capital_name_selector)
population_list = driver.find_elements(By.CSS_SELECTOR,country_population_selector)
total_country = len(country_name_list)

data =[]

# Store Data into Excel File ---- Start From Here ----
for index in range(total_country):
    country_name = country_name_list[index].text
    capital_name = capital_name_list[index].text
    total_population = population_list[index].text
# Create a dictionary for the current country
    country_data = {
        'Country Name': country_name,
        'Capital Name': capital_name,
        'Population': total_population
    }
    data.append(country_data)

file_directory = 'Country_List_JSON_Data'
file_path = os.path.join(file_directory, 'country_data.json')

# Create the directory if it doesn't exist
if not os.path.exists(file_directory):
    os.makedirs(file_directory)

# Open the file in write mode and write the JSON data
with open(file_path, 'w') as file:
    json.dump(data, file)

print('Data stored in JSON format successfully.')


# Close the Browser with the URL
driver.quit()


