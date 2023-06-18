from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

baseUrl="https://www.townscountiespostcodes.co.uk/"
website_title = "Database of information on UK Towns, Counties & Postcodes"
city_section_selector = "#nav ul"
city_lists_selector = "li a"
sub_city_list_selector = "tbody tr"
sub_city_data_selector = "td"

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

city_section = driver.find_elements(By.CSS_SELECTOR,city_section_selector)[2]
WebDriverWait(driver, 10).until(EC.visibility_of(city_section))
city_list = city_section.find_elements(By.CSS_SELECTOR,city_lists_selector)
total_city = len(city_list)


for city_index in range(total_city):
    print(city_index)
    city_name_option = city_list[city_index]
    # Retrieve the text content of the city name option
    # city_name = city_name_option.get_attribute("textContent").strip()
    # print(city_name)
    print(city_name_option)
    city_name_option.click()
    #driver.implicitly_wait(15)
    #time.sleep(10)
    sub_city_list = driver.find_elements(By.CSS_SELECTOR,sub_city_list_selector)
    total_sub_city = len(sub_city_list)
    for sub_city_index in range(1,total_sub_city):
        # Re-find the city name option within the loop to avoid stale element reference
        city_name_option = driver.find_element(By.CSS_SELECTOR, city_lists_selector)
        sub_city = sub_city_list[sub_city_index].find_elements(By.CSS_SELECTOR,sub_city_data_selector)
        sub_city_name = sub_city[1].text
        print(sub_city_name)









# Close the Browser with the URL
#driver.quit()


