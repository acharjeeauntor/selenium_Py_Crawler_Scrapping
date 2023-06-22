import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

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

# Header
header = ['Country Name','Capital Name','Total Population']
# File path to save the CSV
file_directory = 'Country_List_CSV_Data'
if not os.path.exists(file_directory):
    os.makedirs(file_directory)
        
file_path = os.path.join(file_directory, 'country_data.csv')
# Store Data into CSV File ---- Start From Here ----
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    for index in range(total_country):
        country_name = country_name_list[index].text
        capital_name = capital_name_list[index].text
        total_population = population_list[index].text
        csv_writer.writerow([country_name,capital_name,total_population])

# Close the Browser with the URL
driver.quit()


