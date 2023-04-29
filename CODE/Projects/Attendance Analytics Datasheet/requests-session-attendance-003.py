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
        '__VIEWSTATE': '/wEPDwULLTExMTAyMDI0MzAPZBYCAgEPZBYCAg0PPCsADQBkGAEFCUdyaWRWaWV3MQ9nZPhigZbTyQ83UgCf5EqPBzcYVKrN',
        '__VIEWSTATEGENERATOR': '84C2996D',
        '__EVENTVALIDATION': '/wEWAwLa3cuHDQKvmq0hAoznisYGWejYswE+TYAls1lbSGU4NWxP6aU=',
        'TxtRegno': rollno,
        'Button1': 'Submit',
    }

    response = requests.post('https://sadakath.ac.in/attendance2.aspx', headers=headers, data=data)
    soup = BeautifulSoup(response.content, 'html.parser')
    filtered_soupdata_01 = soup.find('table', {'id': 'GridView1'})
    filtered_soupdata_02 = filtered_soupdata_01.find_all('th')
    filtered_soupdata_03 = filtered_soupdata_01.find_all('td')
    filtered_soupdata_04 = filtered_soupdata_02 + filtered_soupdata_03

    head_displayer = []
    for head_data in filtered_soupdata_02:
        head_displayelement = head_data.text
        head_displayer.append(head_displayelement)
    # print(head_displayer)

    data_displayer = []
    for data_data in filtered_soupdata_03:
        data_displayelement = data_data.text
        data_displayer.append(data_displayelement)
    # print(data_displayer)

    head_result_data = ""
    for head_array_data in head_displayer:
        head_result_data = head_result_data + head_array_data + "  "
    print(head_result_data)

    data_result_data = ""
    for data_array_data in data_displayer:
        data_result_data = data_result_data + data_array_data + "  "
    print(data_result_data)

    head_displayer.clear()
    data_displayer.clear()


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
