import requests
from bs4 import BeautifulSoup

index = requests.get('https://www.cnnbrasil.com.br/ultimas-noticias/')

page_content = index.content

soup = BeautifulSoup(page_content, 'html.parser')

atribute_one = {'class': 'a'}

link = soup.find_all('a', class_="home__list__tag")[0]['href']

print(link)