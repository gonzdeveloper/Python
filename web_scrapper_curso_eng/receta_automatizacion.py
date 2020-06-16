
import argparse
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse

import pandas as pd


logger = logging.getLogger(__name__)




def main(filename):
    logger.info('Starting cleaning process')

    # DataFrame
    df = _read_data(filename)
    newspaper_uid = _extraxt_newspaper_uid(filename)
    df = _add_newspaper_uid_column(df, newspaper_uid)
    df = _extract_host(df)
    df = _fill_missing_titles(df)
    df = _extract_host(df)

    return df


def _read_data(filename):
    logger.info(f'Reading file {filename}')

    return pd.read_csv(filename)


def _extraxt_newspaper_uid(filename):
    logger.info('Extract newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info(f'Newspaper uid detected: {newspaper_uid}')
    return newspaper_uid


def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info(f'Fillin newspaper_uid colummn with {newspaper_uid}')
    df['newspaper_uid'] = newspaper_uid

    return df


def _extract_host(df):
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df


def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    # Obtengo las psiciones donde no tengo titulos
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url']
                        .str.extract(r'(?P<missing_titles>[^/]+)$')
                        .applymap(lambda title: title.split('_'))
                        .applymap(lambda title_word_list: ' '.join(title_word_list))
                    )

    # Donde se cumple que tengo missing title quiero que me devuelva la 
    #   columna 'title'
    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to the dirty data',
                        type=str)

    arg = parser.parse_args()

    df = main(arg.filename)
    
    print(df)