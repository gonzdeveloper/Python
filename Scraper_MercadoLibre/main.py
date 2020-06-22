import argparse
import csv
import datetime
import logging
logging.basicConfig(level=logging.INFO)
# Expresiones regularessour 
import re

from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError


import news_page_objects as news
from common import config


logger = logging.getLogger(__name__)
is_well_formated_link = re.compile(r'^https?://.+/.+$') # https://example.com/hola
is_root_path = re.compile(r'^/.+$') #/algun-texto

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    elementos = 0
    i = 0
    inicio = True
    articles = []
    try:
        while i == elementos or inicio:
            inicio = False

            if elementos == 48:
                host = host.replace('.com.uy/_', f'.com.uy/_Desde_{elementos+1}_')
            elif elementos > 48:
                host = host.replace(f'.com.uy/_Desde_{(elementos-48)+1}_', f'.com.uy/_Desde_{elementos+1}_')
            
            logging.info(f'Beginning scraper for {host}')
            logging.info('Finding links in homepage...')

            homepage = news.HomePage(news_site_uid, host)

            print(f'----> Cantidad de links: {len(homepage.article_links)}')

            
            for link in homepage.article_links:
                print(f'--> Vamos por el link: {i}')
                i += 1

                article = _fetch_article(news_site_uid, host, link)

                if article:
                    logger.info('Article fetched!!')
                    articles.append(article)
                    print(f'Titulo: {article.title}')
            
            
            elementos += 48
            # Guardado previo
            # _save_articles(news_site_uid, articles)
    except:
        print('---------------- FIN')
    finally:
        print(f'----> Cantidad de articulos: {len(articles)}')
        # Guardado final
        _save_articles(news_site_uid, articles)



def _save_articles(news_site_uid, articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = f'{news_site_uid}_{now}_articles.csv'

    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    with open(out_file_name, mode='a+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)



def _fetch_article(news_site_uid, host, link):
    logger.info(f'Start fetching article at {link}')

    article = None
    try:
        article = news.ArticlePage(news_site_uid, _build_link(host, link))
    except (HTTPError, MaxRetryError) as e:
        logger.warning(' Error while fetching the article', exc_info=False)


    if article and not article.body:
        logger.warning(' Inavlid article. There is no body')
        return None
    
    return article



# Para construir el link
def _build_link(host, link):
    if is_well_formated_link.match(link):
        return link
    elif is_root_path.match(link):
        return f'{host}{link}'
    else:
        return f'{host}/{link}'
        



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_site_choices)

    args = parser.parse_args()
    _news_scraper(args.news_site)