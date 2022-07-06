# getting the latest patch time

import requests
import datefinder
import datetime
from dateutil import parser
from bs4 import BeautifulSoup

url = "https://en-forum.guildwars2.com/forum/6-game-update-notes/"

def get_soup(url):
    data = requests.get(url)
    return BeautifulSoup(data.text, 'html.parser')

def link_crawler(url, text=""):
    soup = get_soup(url)
    links = soup.find_all("a")
    result = None
    for link in links:
        title = link.get("title")
        href = link.get("href")
        if title and text in title:
            dates = datefinder.find_dates(title)
            for date in dates:
                if date:
                    break
            result = (title, href, date)
            break
    return result

def latest_comment_time(url):
    soup = get_soup(url)
    li = soup.select("div.ipsComment_meta a time")

    for post in li:
        time = parser.isoparse(post.get('datetime'))
    return time

def main():
    global url
    thread = link_crawler(url, "Game Update")
    time = latest_comment_time(thread[1])
    print(time)

if __name__ == "__main__":
    main()