from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver and options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chromedriver_path = "C:\gnirehtet\chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website
driver.get("https://animepahe.com/anime/7d7482ec-adf8-464a-8967-b1b43f18f705")

# Wait for the dynamic content to load
try:
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//div[@class='episode-wrap']"))
    )
except:
    print("Timed out waiting for page to load")
    driver.quit()

# Extract the dynamic content
dynamic_content = driver.find_element_by_xpath("//div[@class='episode-wrap']").text
print(dynamic_content)

# Quit the driver
driver.quit()
