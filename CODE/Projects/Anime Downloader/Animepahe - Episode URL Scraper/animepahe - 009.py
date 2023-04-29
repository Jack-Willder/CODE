from time import time
from requests_html import HTMLSession
time_start = time()

# --  Variables  --
page_list = []
episode_list = []
full_episode_list = []

session = HTMLSession()
url = 'https://animepahe.com/anime/0323e48f-192c-8ca4-6712-f63bcc2cb560'


def page_number_finder(page_count=1):
    page_count = contents[0].text
    page_count = ((str(page_count).replace('(', '')).replace(')', '')).split()
    if len(page_count) > 1:
        for page_counts in page_count:
            if page_counts.isnumeric():
                print("no-of-episodes ", page_counts)
                total_episodes = page_counts
    if int(total_episodes) is not None:
        no_of_pages = 0
        page_count = 0
        while page_count < int(total_episodes):
            no_of_pages += 1
            page_count += 30
        print("no-of-pages ", no_of_pages)
    return int(no_of_pages)


# --  First page scrapper START  --

r = session.get(url=url)
r.html.render(sleep=1, keep_page=True, scrolldown=1)
contents = r.html.find('.episode-count')
total_page_count = page_number_finder()

for pageno in range(2, total_page_count + 1, 1):
    next_page = url + "?page=" + str(pageno)
    print(next_page)
    page_list.append(next_page)

for content in contents:
    print(content.text)

count = int(0)
episode_list = r.html.find('.episode-list')
for episodes in episode_list:
    if episodes.absolute_links is not None:
        episode_links = episodes.absolute_links

for episode_link in episode_links:
    count += 1
    print(count, " - ", episode_link)
    full_episode_list.append(episodes)

# --  First page scrapper END  --

# --  Next page scrapper START  --
episode_list_temp = []
for urls in page_list:
    episode_list.clear()
    r = session.get(url=urls)
    r.html.render(sleep=1, keep_page=True, scrolldown=1)
    contents = r.html.find('.episode-count')
    episode_list = r.html.find('.episode-list')

    for episodes in episode_list:
        if episodes.absolute_links is not None:
            episode_links = episodes.absolute_links

    for episode_link in episode_links:
        count += 1
        print(count, " - ", episode_link)
        episode_list.append(episode_link)
        full_episode_list.append(episodes)


# --  Next page scrapper END  --

print("no-of-episodes ", len(full_episode_list))

# --  Runtime Calculator  --
print("Time Taken - ", time() - time_start)
