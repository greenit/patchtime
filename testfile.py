# just a hello world test file

import requests
import datefinder
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://en-forum.guildwars2.com/forum/6-game-update-notes/"

def main():
    global url
    data = requests.get(url)

    my_data = []

    html = BeautifulSoup(data.text, 'html.parser')
    #print(html)
    links = html.find_all("a")
    #print(articles)
    #print(*html.find_all("a"), sep="\n")
    for link in links:
        title = link.get("title")
        if title and "Game Update" in title:
            print(link)
            break
        #title = article.select('.card-title')[0].get_text()
        #excerpt = article.select('.card-text')[0].get_text()
        #pub_date = article.select('.card-footer small')[0].get_text()

        #my_data.append({"title": title, "excerpt": excerpt, "pub_date": pub_date})
    



    #pprint(my_data)

if __name__ == "__main__":
    main()