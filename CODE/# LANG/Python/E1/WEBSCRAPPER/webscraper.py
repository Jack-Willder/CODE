from bs4 import BeautifulSoup as bs
import requests


def get_soup(site):
    # Making soup
    site = site.text
    soup = bs(site, 'lxml')
    finder(soup)


def finder(soup):
    # Element Finder
    datas = soup.find_all('a', class_ = "wp-block-button__link has-vivid-cyan-blue-to-vivid-purple-gradient-background has-background")
    counter = 0
    for data in datas:
        counter = counter + 1
        datah = data['href']
        # print(datah)
        f = open("URL.txt", 'a')
        f.write(f'''
:: Episode : {counter}\nstart {datah}\nTIMEOUT /T 2 /NOBREAK\n''')
        f.close()



def  main():
    # Getting into site
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    site = requests.get("https://kisstamilanime.com/crayon-shin-chan-season-1-in-tamil-hindi-telugu-hq-576p-amzn-web-dl/", headers=headers)
    # print(site)

    # Checking Site response
    if site.ok:
        print("Access Granted")
        get_soup(site)
    else:
        print("Access Denied")
        
        
main()        