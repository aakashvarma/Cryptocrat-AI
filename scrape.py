import requests
from bs4 import BeautifulSoup
import re
import numpy as np

links_list = []

def link_scrape():
    url = "https://www.coindesk.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    article_tags = soup.find("div", {"id": "content"})
    article_links = article_tags.find_all(class_="fade")

    for a in article_links:
        links = a.get('href')
        links_list.append(links)
    
    return links_list


def text_scrape():
    lin = link_scrape()
    # print (lin)
    try: 
        for l in lin:
            url = l
            page = requests.get(url)

            soup = BeautifulSoup(page.text, 'html.parser')
            content_div_element = soup.find(class_= 'article-content-container')

            for node in content_div_element.findAll('p'):
                print(''.join(node.findAll(text=True)))
    except EOFError:
        print (" EOFError occurred ")
    except OSError:
        print (" OSError occurred ")

text_scrape()
    























