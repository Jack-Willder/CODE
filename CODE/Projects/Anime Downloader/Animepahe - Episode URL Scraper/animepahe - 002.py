# from requests import get, session
# from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch


async def main(url):
    browser = await launch()
    page = await browser.newPage()
    print(type(page))
    # await page.goto(url)

    # # Wait for the content to load
    # await page.waitForSelector('.episode-list')
    #
    # # Extract the Dynamic element
    # element = await page.querySelector('.episode-list')
    # text = await page.evaluate('(element) => element.textContent', element)
    # print(text)

    await browser.close()


asyncio.get_event_loop().run_until_complete(main('https://animepahe.com/anime/7d7482ec-adf8-464a-8967-b1b43f18f705'))




# response = get('https://animepahe.com/anime/7d7482ec-adf8-464a-8967-b1b43f18f705')
# anime_pages = response
# anime_pages = BeautifulSoup(anime_pages.content, "html.parser")
# formatted_anime_pages = str(anime_pages)
# print(type(formatted_anime_pages))
#
# with open(file="TEST.html", mode="w", encoding="utf-8") as f:
#     f.write(str(anime_pages))
#
# episode_context = anime_pages.find_all("div", {"class": "episode-wrap"})
# episode_context = anime_pages.find_all("div", {"class": "episode-list-wrapper"})
# next_page_navigation = anime_pages.find_all("nav", {"class": "Page navigation"})
#
# print(episode_context, next_page_navigation)

