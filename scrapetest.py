import requests
from bs4 import BeautifulSoup

url = "https://www.coindesk.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

article_tags = soup.find("div", {"id": "content"})
# print (article_tags)
artist_name_list_items = article_tags.find_all(class_="fade")
print (artist_name_list_items)


























