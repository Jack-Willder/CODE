import requests
from os import system
from bs4 import BeautifulSoup


def student_profile_extractor(rollno):
    global attendance_profile_variable, head_result, data_result
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
        '__VIEWSTATE': '/wEPDwULLTExMTAyMDI0MzAPZBYCAgEPZBYGAgcPDxYCHgRUZXh0BQYyNTYzNDBkZAILDw8WAh8ABQhTVVJJWUEgTWRkAg0PPCsADQIADxYEHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50AgFkDBQrAAoWCB4ETmFtZQUFQ0NvZGUeCklzUmVhZE9ubHloHgRUeXBlGSsCHglEYXRhRmllbGQFBUNDb2RlFggfAwUFU2Vtbm8fBGgfBRkrAh8GBQVTZW1ubxYIHwMFBVJlZ05vHwRoHwUZKwIfBgUFUmVnTm8WCB8DBQZBZG1uTm8fBGgfBRkrAh8GBQZBZG1uTm8WCB8DBQVTTmFtZR8EaB8FGSsCHwYFBVNOYW1lFggfAwUFVG90YWwfBGgfBRkpWlN5c3RlbS5Eb3VibGUsIG1zY29ybGliLCBWZXJzaW9uPTIuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OR8GBQVUb3RhbBYIHwMFB1ByZXNlbnQfBGgfBRkrBB8GBQdQcmVzZW50FggfAwUGQWJzZW50HwRoHwUZKwQfBgUGQWJzZW50FggfAwUCT0QfBGgfBRkrBB8GBQJPRBYIHwMFClBlcmNlbnRhZ2UfBGgfBRkrBB8GBQpQZXJjZW50YWdlFgJmD2QWBAIBD2QWFGYPDxYCHwAFA1NDU2RkAgEPDxYCHwAFAklWZGQCAg8PFgIfAAUHMjFTQ1M0N2RkAgMPDxYCHwAFBjI1NjM0MGRkAgQPDxYCHwAFCFNVUklZQSBNZGQCBQ8PFgIfAAUCMzlkZAIGDw8WAh8ABQIyM2RkAgcPDxYCHwAFAjE2ZGQCCA8PFgIfAAUBMGRkAgkPDxYCHwAFBTU4Ljk3ZGQCAg8PFgIeB1Zpc2libGVoZGQYAQUJR3JpZFZpZXcxDzwrAAoBCAIBZA0zv/4TQ2vnrw4oIm6uj9eqwllm',
        '__VIEWSTATEGENERATOR': '84C2996D',
        '__EVENTVALIDATION': '/wEWAwKe5t7gBAKvmq0hAoznisYGRJe3whwNdHDPvT3Ve6seaKNzCgw=',
        'TxtRegno': rollno,
        'Button1': 'Submit',
    }

    response = requests.post('https://sadakath.ac.in/attendance2.aspx', headers=headers, data=data)
    soup = BeautifulSoup(response.content, 'html.parser')
    filtered_soupdata_01 = soup.find('table', {'id': 'GridView1'})
    filtered_soupdata_02 = filtered_soupdata_01.find_all('th')
    filtered_soupdata_03 = filtered_soupdata_01.find_all('td')

    head_displayer = []
    head_count_remove = 0
    for head_data in filtered_soupdata_02:
        if head_count_remove == 0 or head_count_remove == 3 or head_count_remove == 6:
            pass
        else:
            head_displayelement = head_data.text
            head_displayer.append(head_displayelement)
        head_count_remove += 1
    # print(head_displayer)

    data_displayer = []
    data_count_remove = 0
    for data_data in filtered_soupdata_03:
        if data_count_remove == 0 or data_count_remove == 3 or data_count_remove == 6:
            pass
        else:
            data_displayelement = data_data.text
            data_displayer.append(data_displayelement)
        data_count_remove += 1
    # print(data_displayer)

    head_reference_data = ""
    data_reference_data = ""

    for head_array_data in head_displayer:
        head_reference_data = head_reference_data + head_array_data + "\n"
    for data_array_data in data_displayer:
        data_reference_data = data_reference_data + data_array_data + "\n"

    head_displayer_data = head_reference_data.splitlines()
    data_displayer_data = data_reference_data.splitlines()

    if len(head_displayer_data) == len(data_displayer_data):
        # print("TRUE - ", rollno)
        length_of_array = len(head_displayer_data)
        head_result = ""
        data_result = ""
        for head_range in range(length_of_array):
            head_result = head_result + head_displayer_data[head_range] + "    "
            data_result = data_result + data_displayer_data[head_range] + "    "
            temp_headlength = len(head_result)
            temp_datalength = len(data_result)
            diff_in_length = temp_headlength - temp_datalength
            if diff_in_length > 0:
                # print(diff_in_length)
                for range01 in range(diff_in_length):
                    data_result += " "
            elif diff_in_length < 0:
                diff_in_length = str(diff_in_length)[1:]
                diff_in_length = int(diff_in_length)
                # print(diff_in_length)
                for range02 in range(diff_in_length):
                    head_result += " "

    head_displayer.clear()
    data_displayer.clear()

    # print(head_result)
    # print(data_result)

    attendance_profile_variable = attendance_profile_variable + data_result + "\n"


attendance_profile_variable = ""
head_result = ""
data_result = ""


if __name__ == "__main__":
    for i in range(48):

        system("cls")
        process_prgress_bar = ((i/48) * 100)
        print("Generating data - ", round(process_prgress_bar, 0), "%")

        i_string = i + 1
        if len(str(i_string)) < 2:
            i_string = "0" + str(int(i_string))
        rollumber = f'21scs{i_string}'
        if i_string == 45 or i_string == 25:
            pass
        else:
            student_profile_extractor(rollumber)
            # print(i_string)

    system("cls")
    attendance_profile_variable = head_result + "\n" + attendance_profile_variable
    print("")
    print(attendance_profile_variable)
