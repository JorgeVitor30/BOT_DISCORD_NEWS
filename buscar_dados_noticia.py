import requests
from bs4 import BeautifulSoup

class BuscarDados:
    def __init__(self, link: str):
        self.link = link
    
    def buscar_new(self):
        index = requests.get(self.link)

        page_content = index.content

        soup = BeautifulSoup(page_content, 'html.parser')

        noticia = soup.find_all('a', class_="home__list__tag")[0]['href']

        return noticia
    