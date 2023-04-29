from requests import get, session
from bs4 import BeautifulSoup

cookies = {
    'SERVERID': 'janna',
    'latest': '5069',
    'res': '720',
    'aud': 'jpn',
    'av1': '0',
    'XSRF-TOKEN': 'eyJpdiI6Iktia3BPZDVyY1NGMFc4eVhsMlJEV0E9PSIsInZhbHVlIjoiT0poaGNsZVA0MkFXQnNqcm9uSTJPNlVObTdPUzllZ1c1QnlNTGJKNFROYmxBSlhiQjVvVjBKbGVaWEhWRXhXL1B6S3Nsdkl5alY1WVN2NkRtV3NqODBFOVdXaWFFZmVpWHBYM3d5ZDhuNU9GT0x3NVpRSzVGYWpzZ1dPbjltZnIiLCJtYWMiOiI3MjBhYzM5NjcxNWRiMzg2ZWY4NDk0ZmEyZjNmZTdiYmZhZWRhZjdlODA5Y2YyNTQwMjIwYTY5YTQzNTU0ZmE0IiwidGFnIjoiIn0%3D',
    'laravel_session': 'eyJpdiI6IkF1M2MzV0V6ODJVRDhpRDlremJJSEE9PSIsInZhbHVlIjoicGJ6cnMyb3lVYy81R0dmeWtwbjFuV2dxc3lvZGdnaVp6ZHJtczF1a0JQdHhvOGJseEx1Q1ZScElRVXhNUEdaZVEvU2pSdUUzUnFmcTc5d0ZYanIxaG00UVBsYUZxV3FaWU9Mc0wyM1dkVytaT1pobytrWDRIUkpRTVpmbEhpdUwiLCJtYWMiOiJkYzFiMWM3YTQxM2FiMTRlMmJhODYxODAyOWMyMGYzYjRhZjU2MzNiMTJkZGEzNTJlMDgxNDNiYzY5NDNlOWJhIiwidGFnIjoiIn0%3D',
    '__cf_bm': '51nnNsUm7KoEstSF3VJyIhzJWjOTaZ1g0EOrU2m_sWI-1679497015-0-AUrUXE8004Vzj+ZYOTzQZfubldxw4qgpL93J/0FBjz0CaJHHT51gG/CupZUol+G1Js/gZVbZA+l85A3VwAKUHylygc6RYGXbyAky08kFCkbdUFhk4hGiqNxx4u4SNepC7g==',
}

headers = {
    'authority': 'animepahe.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'SERVERID=janna; latest=5069; res=720; aud=jpn; av1=0; XSRF-TOKEN=eyJpdiI6Iktia3BPZDVyY1NGMFc4eVhsMlJEV0E9PSIsInZhbHVlIjoiT0poaGNsZVA0MkFXQnNqcm9uSTJPNlVObTdPUzllZ1c1QnlNTGJKNFROYmxBSlhiQjVvVjBKbGVaWEhWRXhXL1B6S3Nsdkl5alY1WVN2NkRtV3NqODBFOVdXaWFFZmVpWHBYM3d5ZDhuNU9GT0x3NVpRSzVGYWpzZ1dPbjltZnIiLCJtYWMiOiI3MjBhYzM5NjcxNWRiMzg2ZWY4NDk0ZmEyZjNmZTdiYmZhZWRhZjdlODA5Y2YyNTQwMjIwYTY5YTQzNTU0ZmE0IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkF1M2MzV0V6ODJVRDhpRDlremJJSEE9PSIsInZhbHVlIjoicGJ6cnMyb3lVYy81R0dmeWtwbjFuV2dxc3lvZGdnaVp6ZHJtczF1a0JQdHhvOGJseEx1Q1ZScElRVXhNUEdaZVEvU2pSdUUzUnFmcTc5d0ZYanIxaG00UVBsYUZxV3FaWU9Mc0wyM1dkVytaT1pobytrWDRIUkpRTVpmbEhpdUwiLCJtYWMiOiJkYzFiMWM3YTQxM2FiMTRlMmJhODYxODAyOWMyMGYzYjRhZjU2MzNiMTJkZGEzNTJlMDgxNDNiYzY5NDNlOWJhIiwidGFnIjoiIn0%3D; __cf_bm=51nnNsUm7KoEstSF3VJyIhzJWjOTaZ1g0EOrU2m_sWI-1679497015-0-AUrUXE8004Vzj+ZYOTzQZfubldxw4qgpL93J/0FBjz0CaJHHT51gG/CupZUol+G1Js/gZVbZA+l85A3VwAKUHylygc6RYGXbyAky08kFCkbdUFhk4hGiqNxx4u4SNepC7g==',
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

response = get('https://animepahe.com/anime/7d7482ec-adf8-464a-8967-b1b43f18f705', cookies=cookies, headers=headers)
anime_pages = response
anime_pages = BeautifulSoup(anime_pages.content, "html.parser")
formatted_anime_pages = str(anime_pages)
print(type(formatted_anime_pages))

with open(file="../TEST.html", mode="w", encoding="utf-8") as f:
    f.write(str(anime_pages))

# episode_context = anime_pages.find_all("div", {"class": "episode-wrap"})
episode_context = anime_pages.find_all("div", {"class": "episode-list-wrapper"})
next_page_navigation = anime_pages.find_all("nav", {"class": "Page navigation"})

print(episode_context, next_page_navigation)
