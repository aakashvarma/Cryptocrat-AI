# firebase class encapsulation / new method


import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pyrebase
import time
import datetime

links_list = []
c = []
title = []


class Scrape:

    def __init__(self):
        pass   

    def link_scrape(self, url):
        self.page = requests.get(url)

        soup = BeautifulSoup(self.page.text, 'html.parser')

        self.article_tags = soup.find("div", {"id": "content"})
        self.article_links = self.article_tags.find_all(class_="fade")

        for a in self.article_links:
            links = a.get('href')
            title.append(a.get('title'))
            links_list.append(links)
        
        return links_list


    def content_scrape(self, url):
        lin = self.link_scrape(url)
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

    def date_time(self):
        return datetime.datetime.now()


if __name__ == '__main__':

    s = Scrape()

    s.link_scrape("https://www.coindesk.com/")

    content = s.content_scrape("https://www.coindesk.com/")
    link = s.link_scrape("https://www.coindesk.com/")
    l = link[0]
    d = str(s.date_time())
    t = title[0]


    config = {
    "apiKey": "AIzaSyAT1llqLb19Zp76JrAOXdgPpb4BGAak1GI",
    "authDomain": "cryptocrat-83570.firebaseapp.com",
    "databaseURL": "https://cryptocrat-83570.firebaseio.com",
    "storageBucket": "cryptocrat-83570.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    data = {
        "url": l,
        "text": content,
        "time": d
    }
    
    db.child("links").child(t).set(data)





















