import requests
from bs4 import BeautifulSoup

cookies = {
    'LRnXh-wdQj': 'i0sPHdUSNaT%5DCZI',
    'cHKuOLxpiEg': 'eSmOzV3g41Bb',
    'mBoiAE': '6zy%40bv%5BQJDcK',
    'roCA_FtJpnf': 'OQ4M8I',
    'dom3ic8zudi28v8lr6fgphwffqoz0j6c': '5cf5c107-4f19-4d75-80b5-8f51a753ae1e%3A2%3A1',
}

headers = {
    'authority': 'kisstamilanime.top',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'LRnXh-wdQj=i0sPHdUSNaT%5DCZI; cHKuOLxpiEg=eSmOzV3g41Bb; mBoiAE=6zy%40bv%5BQJDcK; roCA_FtJpnf=OQ4M8I; dom3ic8zudi28v8lr6fgphwffqoz0j6c=5cf5c107-4f19-4d75-80b5-8f51a753ae1e%3A2%3A1',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; ANE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://kisstamilanime.top/jackie-chan-adventures-season-1-complete-all-episodes-tamil-hindi-telugu-english-1080p-720p-480p-remastered/', cookies=cookies, headers=headers,)
soup = (response.content, 'html.parser')

content = soup.find("div", {"id":"content"})

print(content)
