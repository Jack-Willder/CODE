from time import time
from requests_html import HTMLSession
time_start = time()

# --  Variables  --
page_list = []
episode_list = []
episode_links = []
full_episode_list = []

session = HTMLSession()
url = 'https://animepahe.com/anime/0323e48f-192c-8ca4-6712-f63bcc2cb560?page=13'


# --  First page scrapper START  --

r = session.get(url=url)
r.html.render(sleep=1, keep_page=True, scrolldown=1)
contents = r.html.find('.episode-count')
for content in contents:
    print(content.text)


episode_list = r.html.find('.episode-wrap')

count = int(0)
for episodes in episode_list:
    if episodes.absolute_links is not None:
        episode_links.append(episodes.absolute_links)

for episode_link in episode_links:
    count += 1
    print(count, " - ", episode_link)
    full_episode_list.append(episodes)

# --  First page scrapper END  --


print("no-of-episodes ", len(full_episode_list))

# --  Runtime Calculator  --
print("Time Taken - ", time() - time_start)
