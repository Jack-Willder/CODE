from bs4 import BeautifulSoup
from requests_html import HTMLSession


url = "https://animepahe.com/anime/7d7482ec-adf8-464a-8967-b1b43f18f705"

# Create an HTML session object
session = HTMLSession()

headers = {
    'authority': 'animepahe.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'referer': 'https://animepahe.com/',
    'sec-ch-ua': '"Brave";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

cookies = {
    "XSRF-TOKEN": "eyJpdiI6ImU5ZFpKcE1pSlB3OUZmZDdRWXFDR0E9PSIsInZhbHVlIjoicnVZdm9RRERsU3Q4ZzEyYkcwajhGV0lVRnpXYUxqcGJoUzhRSjFrWmc0QVRaWU5kSFBJUnVlVTQvc1BPd0F0MEhZdFNvckhIbk1SaG12S0JJSkZJZldtdW1xQlJTVFJObUE1b3lPeEpyRnMrdSs4U05jTExxVWh4YWZWT3ZEcWMiLCJtYWMiOiI1ZjVmMzM3MDZiMzBlMGEwMTJmZTk0MDA1MzkzMzFjYzZjNjA2NDEyNDA2Y2U0NjUwYzdkM2FlYmE4ZjY4Y2EyIiwidGFnIjoiIn0=",
    "laravel_session": "eyJpdiI6IkhsdWh1WlI2RkZOM1lkV0F0bXRwZGc9PSIsInZhbHVlIjoiUFVLUkxld2VrdHJXY3RCMVZhbGxqK1BIMnF5cGE5M1A0VzZuTm5SRURwM3d0a1ZhU0k0cU50WXJtMUo0bTFsb1ZvVnpaMEhEYnZNY0tRemFEczVEOWhwTHBQaW5UTXNWcyswZTZldzZoeHFOM2ZyTDZ6Z2lpNHYrSVdOdXZTRUoiLCJtYWMiOiI2ZmZiZDIwYjJlMTA4OGZhYzc3MmQ1MDE2N2U1YTM5YjQzMDhlODI1ODFmMzlkMjhhODA2NTYwYzIwYmEwY2U4IiwidGFnIjoiIn0="
}

# Use the HTMLSession to get the website content
response = session.get(url=url, headers=headers, cookies=cookies)

# print(response.text)

# Render the website content in the background
response.html.render(wait=2)

# Exctract the dersired content from the rendered HTMl
content = response.html.html

content = BeautifulSoup(content, "html.parser")
elemets = content.find("div", {"class": "episode-count"})

print(elemets.text)

session.close()
with open(file="../TEST.html", mode="w", encoding="utf-8") as f:
    f.write(content.text)
