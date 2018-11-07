import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pyrebase
import time
import datetime


def link_scrape(url):
    title = []
    links = []
    result = []
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    article_tags = soup.find("div", {"id": "content"})
    try:
        article_links = article_tags.find_all(class_="fade")
    except AttributeError:
        print ("Attribute error")

    for a in article_links:
        links.append(a.get('href'))
        title.append(a.get('title'))

    result.append(links[0])
    result.append(title[0])
    return result


def content_scrape(url):
    c = []
    lin = link_scrape(url)[0]
    try: 
        url_c = lin
        page = requests.get(url_c)

        soup = BeautifulSoup(page.text, 'html.parser')
        content_div_element = soup.find(class_= 'article-content-container')

        for node in content_div_element.findAll('p'):
            c.append(''.join(node.findAll(text=True)))
        return c
    except EOFError:
        return "EOFError occurred"
    except OSError:
        return "OSError occurred"
    except:
        return "Unexpected error"

def date_time():
        return datetime.datetime.now()


while True:

    text = content_scrape("https://www.coindesk.com/")
    link = link_scrape("https://www.coindesk.com/")[0]
    d = str(date_time())
    t = link_scrape("https://www.coindesk.com/")[1]



    try:
        print (link)
        print (t)
    except OSError:
        print ("OSError")
    except:
        print("error")  


    config = {
    "apiKey": "###",
    "authDomain": "###",
    "databaseURL": "###",
    "storageBucket": "###"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    data = {
        "url": link,
        "text": text,
        "time": d
    }
    
    db.child("links").child(t).set(data)

    time.sleep(60)
