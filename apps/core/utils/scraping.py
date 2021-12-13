import requests
from bs4 import BeautifulSoup


class Lojas:
    def __init__(self, produto):
        self.produto = produto

    def __response(self):
        response = requests.get(self.produto.url)
        if response.status_code == 200:
            return response.content

    def __soup(self):
        response = self.__response()
        if response:
            return BeautifulSoup(response, 'html.parser')

    def __dispacher(self):
        if 'mercadolivre' in self.produto.url:
            return MercadoLivre

    def data(self):
        try:
            soup = self.__soup()
            loja = self.__dispacher()
            if soup:
                return loja(soup).data()

        except:
            return {
                'nome': None,
                'preco': None,
                'imagem': None
            }


class MercadoLivre:
    def __init__(self, soup: BeautifulSoup) -> dict:
        self.soup = soup

    def data(self):
        nome = self.soup.find("h1").text
        preco = self.soup.find('span', {'class': ['price-tag', 'ui-pdp-price__part']}).text.split('R$')[1]
        imagem = self.soup.find("img", {'class': "ui-pdp-image ui-pdp-gallery__figure__image"}).attrs['src']
        return {
            'nome': nome,
            'preco': preco,
            'imagem': imagem
        }
