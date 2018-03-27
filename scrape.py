import requests
from bs4 import BeautifulSoup
import re

def link_scrape():
    url = "https://www.coindesk.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    article_tags = soup.find("div", {"id": "content"})
    article_links = article_tags.find_all(class_="fade")

    for a in article_links:
        links = a.get('href')
        print (links)

def text_scrape():
    url = "https://www.coindesk.com/ford-patent-envisions-car-car-crypto-transactions/"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    content_div_element = soup.find(class_= 'article-content-container')

    for node in content_div_element.findAll('p'):
        print(''.join(node.findAll(text=True)))
    























