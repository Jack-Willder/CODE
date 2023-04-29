import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

cookies = {
    'SERVERID': 'janna',
    'latest': '5079',
    '__cf_bm': '3SEYKShpFlB2jAT405xQ9Y4fPNjQA8iHLjkIft2hevM-1679579471-0-ARev87xDm2TX3yhN6kjWW4hNikLwc/KErtYHzjLjBCu+9CbTag1UOj1KwLIEBu4SZE5BnRDe6gbdpfgxyWXWIrYnDxjM385hcQO7VqHSQXjcjOqdAb7ALChkYCNFEm+drg==',
    'XSRF-TOKEN': 'eyJpdiI6IitQQlFXU3hZYnhXOHhjR20rVVZqa3c9PSIsInZhbHVlIjoiWGhMRWg0a25LZkErck1Ib29uMEpWOE5MN1huTCtaRlo5VU5XUEFHUCtjT0ZVY3E2WVZJYUhYUlBTZk1nV1pQaHVHMnhaSk1ValVDTytzeEx4c25uWkh3enNBSjVML3hvYkxqS09Ta01QOXNSUmM4V0pza25YNE5DbWNnNkJkbDEiLCJtYWMiOiI5NGQ0OGVjMDAyNGRiNTVmOGRjZDY4ZmUyNWVhODQwMjliODQ2ZDY5NTZkNTM0OTdkMDMzYjMyNzFmN2JkMzgzIiwidGFnIjoiIn0%3D',
    'laravel_session': 'eyJpdiI6IlFKcnB4Y3ErZ3owWUpYbHYyVjVFWGc9PSIsInZhbHVlIjoiQ1hHMHBEeGdSNllRY0l4b0E2K0JoQVcyRVpHV0RDeWFMaDdWLzNLYWtWRkxKekU1M2crOG9mcFAxZlo0bCtQdHNkaDVwQmVjUUM3VHlFdFo5bjVDMVpSUkpISEJIRGRZM3FSVFd4aitXRVVGMXpDMG8zcjl0SVhaVlNRUktYakgiLCJtYWMiOiJlNGI3ZDcwODVlZmQ3NmNmMDllMjNlZmQyOWFjNDc2MDYxMTg0NzI0MGMzMWM5N2FjZGU4MjcxN2Y0NDQwMTQyIiwidGFnIjoiIn0%3D',
}

headers = {
    'authority': 'animepahe.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'SERVERID=janna; latest=5079; __cf_bm=3SEYKShpFlB2jAT405xQ9Y4fPNjQA8iHLjkIft2hevM-1679579471-0-ARev87xDm2TX3yhN6kjWW4hNikLwc/KErtYHzjLjBCu+9CbTag1UOj1KwLIEBu4SZE5BnRDe6gbdpfgxyWXWIrYnDxjM385hcQO7VqHSQXjcjOqdAb7ALChkYCNFEm+drg==; XSRF-TOKEN=eyJpdiI6IitQQlFXU3hZYnhXOHhjR20rVVZqa3c9PSIsInZhbHVlIjoiWGhMRWg0a25LZkErck1Ib29uMEpWOE5MN1huTCtaRlo5VU5XUEFHUCtjT0ZVY3E2WVZJYUhYUlBTZk1nV1pQaHVHMnhaSk1ValVDTytzeEx4c25uWkh3enNBSjVML3hvYkxqS09Ta01QOXNSUmM4V0pza25YNE5DbWNnNkJkbDEiLCJtYWMiOiI5NGQ0OGVjMDAyNGRiNTVmOGRjZDY4ZmUyNWVhODQwMjliODQ2ZDY5NTZkNTM0OTdkMDMzYjMyNzFmN2JkMzgzIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlFKcnB4Y3ErZ3owWUpYbHYyVjVFWGc9PSIsInZhbHVlIjoiQ1hHMHBEeGdSNllRY0l4b0E2K0JoQVcyRVpHV0RDeWFMaDdWLzNLYWtWRkxKekU1M2crOG9mcFAxZlo0bCtQdHNkaDVwQmVjUUM3VHlFdFo5bjVDMVpSUkpISEJIRGRZM3FSVFd4aitXRVVGMXpDMG8zcjl0SVhaVlNRUktYakgiLCJtYWMiOiJlNGI3ZDcwODVlZmQ3NmNmMDllMjNlZmQyOWFjNDc2MDYxMTg0NzI0MGMzMWM5N2FjZGU4MjcxN2Y0NDQwMTQyIiwidGFnIjoiIn0%3D',
    'dnt': '1',
    'referer': 'https://animepahe.com/anime/71bea372-83ee-7ef7-84c1-ded2b38faecc',
    'sec-ch-ua': '"Brave";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'm': 'release',
    'id': '71bea372-83ee-7ef7-84c1-ded2b38faecc',
    'sort': 'episode_asc',
    'page': '1',
}
response = requests.get('https://animepahe.com/api', params=params, cookies=cookies, headers=headers)

if response.status_code == 200:
    # print(response.content)
    print(response.json())
    with open(file="../TEST.json", mode="w", encoding="utf-8") as f:
        f.write(str(response.json()))
else:
    print('Error: ' + str(response.status_code))
