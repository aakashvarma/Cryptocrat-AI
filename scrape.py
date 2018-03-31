import requests
from bs4 import BeautifulSoup
import re
import numpy as np

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
                print (c)
        except EOFError:
            print (" EOFError occurred ")
        except OSError:
            print (" OSError occurred ")


if __name__ == '__main__':
    s = Scrape()  
    s.content_scrape("https://www.coindesk.com/")






















