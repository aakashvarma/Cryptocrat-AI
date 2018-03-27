import requests
from bs4 import BeautifulSoup
import re

def link_scrape():
    url = "https://www.coindesk.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    article_tags = soup.find("div", {"id": "content"})
    # print (article_tags)
    article_links = article_tags.find_all(class_="fade")
    # print (article_links)

    for a in article_links:
        # print (a.contents)
        links = a.get('href')
        print (links)

def text_scrape():
    























