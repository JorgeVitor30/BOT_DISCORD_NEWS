import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.cnnbrasil.com.br/ultimas-noticias/')

page_content = page.content

soup = BeautifulSoup(page_content, 'html.parser')


atributos = {'class': 'a'}

link = soup.find_all('a', class_="home__list__tag")[0]


print(link)