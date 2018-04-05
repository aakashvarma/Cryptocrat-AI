import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pyrebase

links_list = []
c = []

class Scrape:

    def __init__(self):
        pass   

    def link_scrape(self, url):
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')

        article_tags = soup.find("div", {"id": "content"})
        article_links = article_tags.find_all(class_="fade")

        for a in article_links:
            links = a.get('href')
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
            return " EOFError occurred "
        except OSError:
            return " OSError occurred "
        except:
            return " Unexpected error "



if __name__ == '__main__':
    s = Scrape()  
    content = s.content_scrape("https://www.coindesk.com/")
    link = s.link_scrape("https://www.coindesk.com/")
    

    config = {
    "apiKey": "AIzaSyAT1llqLb19Zp76JrAOXdgPpb4BGAak1GI",
    "authDomain": "cryptocrat-83570.firebaseapp.com",
    "databaseURL": "https://cryptocrat-83570.firebaseio.com",
    "storageBucket": "cryptocrat-83570.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    data = {
        "url": link,
        "text": content
    }
    db.child("links").child("test2").set(data)





















