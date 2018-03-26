import requests
from bs4 import BeautifulSoup

url = "https://www.coindesk.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# title = soup.find(class_='menu-item')
article_tags = soup.find("div", {"id": "content"})
# print (article_tags)
article_list = article_tags.find_all('a')
print (article_list)
































