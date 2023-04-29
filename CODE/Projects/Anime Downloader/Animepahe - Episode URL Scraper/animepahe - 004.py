# from bs4 import BeautifulSoup
from requests_html import HTMLSession


url = "https://animepahe.com/anime/7d7482ec-adf8-464a-8967-b1b43f18f705"

# Create an HTML session object
session = HTMLSession()

# Use the HTMLSession to get the website content
response = session.get(url=url)

# Render the website content in the background
response.html.render(wait=30)

# Exctract the dersired content from the rendered HTMl
content = response.html.html

print(type(content))
print(content)

session.close()

with open(file="../TEST.html", mode="w", encoding="utf-8") as f:
    f.write(content)
