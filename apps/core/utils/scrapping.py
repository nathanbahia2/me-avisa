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

    def data(self):
        soup = self.__soup()
        if soup:
            return MercadoLivre(soup).data()


class MercadoLivre:
    def __init__(self, soup):
        self.soup = soup

    def data(self):
        produto = self.soup.find("h1").text
        preco = self.soup.find('span', {'class': ['price-tag', 'ui-pdp-price__part']}).text.split('R$')[1]
        imagem = self.soup.find("img", {'class': "ui-pdp-image ui-pdp-gallery__figure__image"}).attrs['src']

        return {
            'nome': produto,
            'preco': preco,
            'imagem': imagem,
        }
