import requests
from bs4 import BeautifulSoup


def student_profile_extractor(rollno):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://sadakath.ac.in',
        'Referer': 'https://sadakath.ac.in/attendance2.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    data = {
        '__VIEWSTATE': '/wEPDwULLTExMTAyMDI0MzAPZBYCAgEPZBYGAgcPDxYCHgRUZXh0BQYyNTYzNDBkZAILDw8WAh8ABQhTVVJJWUEgTWRkAg0PPCsADQIADxYEHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50AgFkDBQrAAoWCB4ETmFtZQUFQ0NvZGUeCklzUmVhZE9ubHloHgRUeXBlGSsCHglEYXRhRmllbGQFBUNDb2RlFggfAwUFU2Vtbm8fBGgfBRkrAh8GBQVTZW1ubxYIHwMFBVJlZ05vHwRoHwUZKwIfBgUFUmVnTm8WCB8DBQZBZG1uTm8fBGgfBRkrAh8GBQZBZG1uTm8WCB8DBQVTTmFtZR8EaB8FGSsCHwYFBVNOYW1lFggfAwUFVG90YWwfBGgfBRkpWlN5c3RlbS5Eb3VibGUsIG1zY29ybGliLCBWZXJzaW9uPTIuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OR8GBQVUb3RhbBYIHwMFB1ByZXNlbnQfBGgfBRkrBB8GBQdQcmVzZW50FggfAwUGQWJzZW50HwRoHwUZKwQfBgUGQWJzZW50FggfAwUCT0QfBGgfBRkrBB8GBQJPRBYIHwMFClBlcmNlbnRhZ2UfBGgfBRkrBB8GBQpQZXJjZW50YWdlFgJmD2QWBAIBD2QWFGYPDxYCHwAFA1NDU2RkAgEPDxYCHwAFAklWZGQCAg8PFgIfAAUHMjFTQ1M0N2RkAgMPDxYCHwAFBjI1NjM0MGRkAgQPDxYCHwAFCFNVUklZQSBNZGQCBQ8PFgIfAAUCMzhkZAIGDw8WAh8ABQIyM2RkAgcPDxYCHwAFAjE1ZGQCCA8PFgIfAAUBMGRkAgkPDxYCHwAFBTYwLjUzZGQCAg8PFgIeB1Zpc2libGVoZGQYAQUJR3JpZFZpZXcxDzwrAAoBCAIBZD0N3n92xSt+/NHBO4b5zElV7CaD',
        '__VIEWSTATEGENERATOR': '84C2996D',
        '__EVENTVALIDATION': '/wEWAwLd94jKDQKvmq0hAoznisYGpqhpx4Uw6P9VOpCJMCFLWlJuXLU=',
        'TxtRegno': rollno,
        'Button1': 'Submit',
    }

    response = requests.post('https://sadakath.ac.in/attendance2.aspx', headers=headers, data=data)
    soup = BeautifulSoup(response.content, 'html.parser')
    soupdata = soup.find('table', {'id': 'GridView1'})
    print(soupdata)


if __name__ == "__main__":
    for i in range(48):
        i_string = i + 1
        if len(str(i_string)) < 2:
            i_string = "0" + str(int(i_string))
        rollumber = f'21scs{i_string}'
        if i_string == 45 or i_string == 25:
            print("Left")
        else:
            student_profile_extractor(rollumber)
            # print(i_string)
