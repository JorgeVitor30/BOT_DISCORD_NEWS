import requests
from bs4 import BeautifulSoup

page = requests.get('https://g1.globo.com/ultimas-noticias/')

soup = BeautifulSoup(page.content, 'html.parser')


atributos = {'class': 'a'}

link = soup.find_all('a', class_="feed-post-link gui-color-primary gui-color-hover")[0]


print(link)