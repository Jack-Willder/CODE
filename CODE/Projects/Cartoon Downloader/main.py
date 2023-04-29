# This part of the code uses pure request module
"""
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
#
#
# url = "https://new.kisstamilanime.com/crayon-shin-chan-season-3-episodes-in-tamil-hindi-telugu-720p-480p/"
# s = HTMLSession()
# r = s.get(url=url)
#
# r.html.render(sleep=1)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# episodes = soup.find_all('a', {'class': 'wp-block-button__link has-white-color has-vivid-cyan-blue-to-vivid-purple-gradient-background has-text-color has-background'})
#
#
# link_counter = 0
# for episode in episodes:
#     if episode.get("href") is not None:
#         print(episode.get("href"))
#         link_counter += 1
# print(f"Number of links >{link_counter}<")
"""

# This part of the code uses pure selenium module

# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

soup = BeautifulSoup()

driver = webdriver.Edge()
driver.get(url="https://new.kisstamilanime.com/crayon-shin-chan-season-3-episodes-in-tamil-hindi-telugu-720p-480p/")
driver.maximize_window()

container_number = 3
button = driver.find_elements(by=By.CSS_SELECTOR, value='div.wp-container-1')
print(button)
