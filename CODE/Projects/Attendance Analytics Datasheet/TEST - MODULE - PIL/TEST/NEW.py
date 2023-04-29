import time
import requests
from os import system
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


def student_profile_extractor(rollno):
    global attendance_profile_variable, head_result, data_result, max_array_length, remaining_head_list, remaining_data_list, onetime_head_runner_variable, remaining_data_length
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
        '__VIEWSTATE': '/wEPDwULLTExMTAyMDI0MzAPZBYCAgEPZBYCAg0PPCsADQBkGAEFCUdyaWRWaWV3MQ9nZL/5xRetOc6eiIkyHnR+CXRwMQl/',
        '__VIEWSTATEGENERATOR': '84C2996D',
        '__EVENTVALIDATION': '/wEWAwKEm6umBgKvmq0hAoznisYG3qRwEcGzOaDnMs46fIOQpv3TJ6Q=',
        'TxtRegno': rollno,
        'Button1': 'Submit',
    }

    response = requests.post('https://sadakath.ac.in/attendance2.aspx', headers=headers, data=data)
    soup = BeautifulSoup(response.content, 'html.parser')
    filtered_soupdata_01 = soup.find('table', {'id': 'GridView1'})
    filtered_soupdata_02 = filtered_soupdata_01.find_all('th')
    filtered_soupdata_03 = filtered_soupdata_01.find_all('td')

    """*  HEAD  *"""

    head_displayer = []
    head_count_remove = 0
    for head_data in filtered_soupdata_02:
        if head_count_remove == 0 or head_count_remove == 1 or head_count_remove == 3 or head_count_remove == 5 or head_count_remove == 6:
            pass
        else:
            if head_count_remove <= 4:
                head_displayelement = head_data.text
                head_displayer.append(head_displayelement)
            if 4 < head_count_remove:
                if onetime_head_runner_variable < int(len(filtered_soupdata_02) - 7):
                    remaining_head_list.append(head_data.text)
                    onetime_head_runner_variable += 1
        head_count_remove += 1
    # print(head_displayer)

    """*  DATA  *"""

    data_displayer = []
    data_count_remove = 0
    for data_data in filtered_soupdata_03:
        if data_count_remove == 0 or data_count_remove == 1 or data_count_remove == 3 or data_count_remove == 5 or data_count_remove == 6:
            pass
        else:
            if data_count_remove <= 4:
                data_displayelement = data_data.text
                data_displayer.append(data_displayelement)
            if 4 < data_count_remove:
                remaining_data_list.append(data_data.text)
        data_count_remove += 1
        remaining_data_length = int(len(filtered_soupdata_02) - 6)
    # print(data_displayer)

    # print(remaining_head_list)
    # print(remaining_data_list)

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

    """*  This part of the code is used to add the remaining table elements  *"""

    attendance_profile_variable = attendance_profile_variable + data_result + "\n"


def max_length_finder(max_data):
    global max_array_length, max_array
    max_data = max_data.splitlines()
    for max_data_element in range(len(max_data)):
        max_array.append(len(max_data[max_data_element]))
        # print(len(max_data[max_data_element]))
    max_array_length = max(max_array)
    remaining_gap_filler(max_array_length, max_data)


def remaining_gap_filler(gap_length, gap_data_before):
    global head_result, data_result, attendance_profile_variable, temp_data_result
    pass
    data_result = ""
    for gap_element in gap_data_before:
        # print("val - ", len(gap_element), " > ", end="")
        if len(gap_element) < gap_length:
            required_gap_length = gap_length - len(gap_element)
            for gap_adder in range(required_gap_length):
                gap_element += " "
        # print(len(gap_element))
        data_result = data_result + gap_element + "\n"
    if len(head_result) < gap_length:
        for head_gap_add in range(int(gap_length - len(head_result))):
            head_result += " "

    # print(attendance_profile_variable)
    # print(data_result)
    # print(head_result)

    data_result = data_result.splitlines()
    # print(data_result)

    """*  Adding the remaining Elements  *"""
    temp_count_number_01 = 0
    temp_count_number_02 = 1
    temp_count_number_03 = 1
    for remaining_head in remaining_head_list:
        data_result01.clear()
        if temp_count_number_01 > len(remaining_head_list):
            temp_count_number_01 = temp_count_number_02
            temp_count_number_03 += 1
            temp_count_number_02 = temp_count_number_03

        head_result = head_result + remaining_head + "    "
        length_0f_remaining_head = len(head_result)
        length_0f_remaining_data = len(data_result)
        for temp_data_length in range(length_0f_remaining_data):
            data_result[temp_data_length] += remaining_data_list[temp_count_number_01]
            length_0f_temp_data_result = len(data_result[temp_data_length])

            if (temp_count_number_01 + 3) < (len(remaining_data_list)):
                temp_count_number_01 += 3

            # print("len of temp count 02 - ", temp_count_number_01)

            if length_0f_temp_data_result < length_0f_remaining_head:
                temp_gap_length = length_0f_remaining_head - length_0f_temp_data_result

            for _ in range(temp_gap_length):
                data_result[temp_data_length] += " "

            data_result01.append(data_result[temp_data_length])

    attendance_profile_variable = head_result + "\n"
    for temp_data_result_01 in data_result01:
        attendance_profile_variable = attendance_profile_variable + temp_data_result_01 + "\n"


def data_list_sorter(temp_attendance_profile_variable):
    temp_reference_list = temp_attendance_profile_variable.splitlines()
    temp_sort_list_01 = temp_attendance_profile_variable.splitlines()
    temp_sort_list_02 = []
    temp_sort_list_03 = []
    temp_sort_list_04 = []
    temp_reference_list.pop(0)
    temp_sort_list_01.pop(0)
    for temp_sort_element in temp_sort_list_01:
        temp_sort_element = temp_sort_element[44:]
        temp_sort_element = temp_sort_element.split()
        temp_sort_element = temp_sort_element[0]
        temp_sort_list_02.append(temp_sort_element)

    """*  Sorting mechanism for the Attendance list  *"""
    temp_a = list(set(temp_sort_list_02))
    temp_d = []

    for temp_i in range(0, len(temp_a)):
        temp_b = temp_a[temp_i]
        temp_c = temp_b.split(".")
        if len(temp_c[0]) < 2:
            temp_e = "0" + str(temp_a[temp_i])
            temp_d.append(temp_e)
        else:
            temp_d.append(temp_a[temp_i])

    for temp_i in range(0, len(temp_sort_list_02)):
        temp_b = temp_sort_list_02[temp_i]
        temp_c = temp_b.split(".")
        if len(temp_c[0]) < 2:
            temp_e = "0" + str(temp_sort_list_02[temp_i])
            temp_sort_list_04.append(temp_e)
        else:
            temp_sort_list_04.append(temp_sort_list_02[temp_i])

    temp_sort_list_02 = temp_sort_list_04
    temp_d.sort()

    """*  Main Sorting Algorithm  *"""
    for temp_i in temp_d:
        for j in range(0, len(temp_sort_list_02)):
            if temp_sort_list_02[j] == temp_i:
                temp_sort_list_03.append(temp_sort_list_01[j])

    """*  Creating Decending output list  *"""
    temp_count_number_i = len(temp_sort_list_03)
    for temp_i in range(len(temp_sort_list_03)):
        temp_count_number_i -= 1
        temp_sort_list.append(temp_sort_list_03[temp_count_number_i])


def data_list_column_spliter():
    global final_rollno, final_name, final_absent, final_od, final_percent
    temp_test_data_print = []
    for temp_data in temp_sort_list:
        temp_splited_data = temp_data.split("  ")
        for temp_split in temp_splited_data:
            if temp_split is not None and not temp_split == '' and not temp_split == ' ':
                temp_test_data_print.append(temp_split)
        final_list_rollno.append(temp_test_data_print[0])
        final_list_name.append(temp_test_data_print[1])
        final_list_absent.append(temp_test_data_print[2])
        final_list_od.append(temp_test_data_print[3])
        final_list_percent.append(temp_test_data_print[4])
        # print(temp_test_data_print)
        temp_test_data_print.clear()

    for temp_rollno in final_list_rollno:
        if " " in temp_rollno:
            temp_rollno = temp_rollno.replace(" ", "")
        final_rollno = final_rollno + temp_rollno + "\n"

    for temp_name in final_list_name:
        final_name = final_name + temp_name + "\n"

    for temp_absent in final_list_absent:
        if " " in temp_absent:
            temp_absent = temp_absent.replace(" ", "")
        final_absent = final_absent + temp_absent + "\n"

    for temp_od in final_list_od:
        if " " in temp_od:
            temp_od = temp_od.replace(" ", "")
        final_od = final_od + temp_od + "\n"

    for temp_percent in final_list_percent:
        if " " in temp_percent:
            temp_percent = temp_percent.replace(" ", "")
        final_percent = final_percent + temp_percent + "\n"


def final_image_processor():
    global final_rollno, final_name, final_absent, final_od, final_percent
    final_rank = """01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
"""

    new = Image.open("BG-old.png")

    d = ImageDraw.Draw(new)

    tuple_time = time.localtime()
    local_time = time.strftime("%d_%m_%Y", tuple_time)

    font = ImageFont.truetype(font="font/Roboto-Medium.ttf", size=30)
    fill = (255, 255, 255)

    d.text((170 + 0, 448 + 420), text="Top 10 - ", fill=(150, 150, 150), font=font, spacing=15)
    d.text((170 + 150, 448), text=final_rank, fill=(249, 255, 33), font=font, spacing=15)
    d.text((170 + 300, 448), text=final_rollno, fill=fill, font=font, spacing=15)
    d.text((350 + 300, 448), text=final_name, fill=fill, font=font, spacing=15)
    d.text((950 + 300, 448), text=final_absent, fill=fill, font=font, spacing=15)
    d.text((1100 + 300, 448), text=final_od, fill=fill, font=font, spacing=15)
    d.text((1200 + 300, 448), text=final_percent, fill=fill, font=font, spacing=15)

    new.save("{}.png".format(local_time))


attendance_profile_variable = ""
head_result = ""
data_result = ""
data_result01 = []
temp_data_result = ""
max_array_length = ""
max_array = []
remaining_head_list = []
remaining_data_list = []
onetime_head_runner_variable = 0
remaining_data_length = 0
adder_length_of_eachremaininghead = []
temp_sort_list = []
# --------------------------------------------------
final_list_rollno = []
final_list_name = []
final_list_absent = []
final_list_od = []
final_list_percent = []
final_rollno = ""
final_name = ""
final_absent = ""
final_od = ""
final_percent = ""

if __name__ == "__main__":
    for i in range(48):

        process_prgress_bar = ((i / 48) * 100)
        print("Generating data - ", round(process_prgress_bar, 0), "%")

        i_string = i + 1
        if len(str(i_string)) < 2:
            i_string = "0" + str(int(i_string))
        rollumber = f'21scs{i_string}'
        if i_string == 45 or i_string == 25:
            pass
        else:
            student_profile_extractor(rollumber)

    """*  After the Iteration part  *"""

    max_length_finder(attendance_profile_variable)
    print("The Maximum length of the Array element - ", max_array_length)

    data_list_sorter(attendance_profile_variable)

    # <  SPLITING THE LIST INTO COLUMNS  >

    data_list_column_spliter()
    print(final_rollno)
    print(final_name)
    print(final_absent)
    print(final_od)
    print(final_percent)

    final_image_processor()
