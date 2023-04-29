import requests
from bs4 import BeautifulSoup

formurl = 'https://sadakath.ac.in/attendance2.aspx'

rollnumber = 47

studentnumber = f'21scs{rollnumber}'

payload = {
    # '__VIEWSTATE': '%2FwEPDwULLTExMTAyMDI0MzAPZBYCAgEPZBYGAgcPDxYCHgRUZXh0BQEtZGQCCw8PFgIfAAUBLWRkAg0PPCsADQIADxYGHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50Zh4HVmlzaWJsZWhkDBQrAAoWCB4ETmFtZQUFQ0NvZGUeCklzUmVhZE9ubHloHgRUeXBlGSsCHglEYXRhRmllbGQFBUNDb2RlFggfBAUFU2Vtbm8fBWgfBhkrAh8HBQVTZW1ubxYIHwQFBVJlZ05vHwVoHwYZKwIfBwUFUmVnTm8WCB8EBQZBZG1uTm8fBWgfBhkrAh8HBQZBZG1uTm8WCB8EBQVTTmFtZR8FaB8GGSsCHwcFBVNOYW1lFggfBAUFVG90YWwfBWgfBhkpWlN5c3RlbS5Eb3VibGUsIG1zY29ybGliLCBWZXJzaW9uPTIuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OR8HBQVUb3RhbBYIHwQFB1ByZXNlbnQfBWgfBhkrBB8HBQdQcmVzZW50FggfBAUGQWJzZW50HwVoHwYZKwQfBwUGQWJzZW50FggfBAUCT0QfBWgfBhkrBB8HBQJPRBYIHwQFClBlcmNlbnRhZ2UfBWgfBhkrBB8HBQpQZXJjZW50YWdlZBgBBQlHcmlkVmlldzEPPCsACgEIZmSAMdMBahpWytQ5SS1PyQ7pnNpa0w%3D%3D',
    # '__VIEWSTATEGENERATOR': '84C2996D',
    # '__EVENTVALIDATION': '%2FwEWAwK8yP7eDgKvmq0hAoznisYGSJegRQiF9up0hmcnuAmu4PuaPYE%3D',
    'TxtRegno': studentnumber,
    # 'Button1': 'Submit'
}

with requests.session() as s:
    s.post(formurl, data=payload)
    r = requests.get(formurl)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())
