import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coindesk.com/ford-patent-envisions-car-car-crypto-transactions/"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
content_div_element = soup.find(class_= 'article-content-container')
content = content_div_element.find_all('p')

for node in content_div_element.findAll('p'):
    print(''.join(node.findAll(text=True)))












