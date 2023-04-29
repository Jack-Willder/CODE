import requests
from bs4 import BeautifulSoup as bsp

test_session = requests.session()

r = test_session.get("https://sadakath.ac.in/attendance2.aspx")
print(r.status_code)

bs = bsp(r.content, "html.parser")

viewstate = bs.select('#__VIEWSTATE')
eventvalidation = bs.select('#__EVENTVALIDATION')


print(viewstate, eventvalidation)

# abc = bsp.find("input", {"name":"__VIEWSTATE"}).attrs['value']
# bcd = bsp.find("input", {"name":"__EVENTVALIDATION"}).attrs['value']
# print(abc, bcd)
