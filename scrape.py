# firebase class encapsulation / new method
# Fix the list of text appending and printing
# scraoe the time and date from the site iself
# select the last element of the list to get the new link ,,,,,   but the list size increases a lot .... so try to append the list inthe starting
# env files for config of firebase
# use encapsulation



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
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')

        article_tags = soup.find("div", {"id": "content"})
        try:
            article_links = article_tags.find_all(class_="fade")
        except AttributeError:
            print ("Attribute error")

        for a in article_links:
            links = a.get('href')
            title.append(a.get('title'))
            links_list.append(links)
        
        return links_list


    def content_scrape(self):
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

    def date_time(self):
        return datetime.datetime.now()


if __name__ == '__main__':


    while True:

        s = Scrape()
        link = s.link_scrape("https://www.coindesk.com/")
        content = s.content_scrape()


        l = link[0]
        print (l)
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

        time.sleep(60)





















