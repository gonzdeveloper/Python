
import bs4
import requests

from common import config

class NewsPage:

    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None

        # Llamo al metodo propio para armar el arbol de nodos
        self._visit(url)



    def _select(self, query_string):
        nodes = self._html.select(query_string)
        if not nodes:
            return None

        return nodes

        

    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')


class HomePage(NewsPage):

    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)


    @property
    def article_links(self):
        link_list = []

        # i = 0

        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

            # i = i + 1
            # if i>4:
            #     break

        
        # Elimino los elementos repetidos
        return set(link['href'] for link in link_list)


class ArticlePage(NewsPage):

    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)
        self._url = url

    @property
    def url(self):
        return self._url

    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        return result[0].text if result != None else ''

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        return result[0].text if result != None else ''

    @property
    def price(self):
        result = self._select(self._queries['article_price'])
        return result[0].text if result != None else ''

    @property
    def localidad(self):
        result = self._select(self._queries['localidad'])
        return result[0].text if result != None else ''

    @property
    def fichatecnica(self):
        result = self._select(self._queries['fichatecnica'])
        return result[0].text if result != None else ''




        

        


    




