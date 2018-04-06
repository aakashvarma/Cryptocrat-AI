import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pyrebase
import time
import datetime



def link_scrape(url):
    links = []
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    article_tags = soup.find("div", {"id": "content"})
    try:
        article_links = article_tags.find_all(class_="fade")
    except AttributeError:
        print ("Attribute error")

    for a in article_links:
        links.append(a.get('href'))
    
    print (links)
    print ("_________________________________________________________________________")


def content_scrape():
    lin = links_list
    try: 
        for l in lin:
            url_c = l
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

while True:
    link_scrape("https://www.coindesk.com/")
    time.sleep(60)


# while True:

#     link = link_scrape("https://www.coindesk.com/")
#     content = content_scrape()


#     l = link[0]
#     print (l)
#     t = title[0]


#     config = {
#     "apiKey": "AIzaSyAT1llqLb19Zp76JrAOXdgPpb4BGAak1GI",
#     "authDomain": "cryptocrat-83570.firebaseapp.com",
#     "databaseURL": "https://cryptocrat-83570.firebaseio.com",
#     "storageBucket": "cryptocrat-83570.appspot.com"
#     }

#     firebase = pyrebase.initialize_app(config)
#     db = firebase.database()

#     data = {
#         "url": l,
#         "text": content
#     }
    
#     db.child("links").child(t).set(data)

#     time.sleep(60)
