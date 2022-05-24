import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import string
import os.path 
import matplotlib.pyplot as plt
import ast

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

# from google.colab import drive, auth
# # Mount Google Drive
# drive.mount("/content/drive")

base_dir = './'

raw_list = []

def crawl(mpa):
    for current_page in tqdm(range(1, 9952, 50)):
        response = requests.get('https://www.imdb.com/search/title/?' 
                                + 'title_type=feature,tv_movie,tv_special,documentary,short,tv_short' 
                                + '&certificates=US%3A' + mpa 
                                + '&start=' + str(current_page))

        soup = BeautifulSoup(response.text, 'html.parser')

        for i in range(len(soup.select('h3.lister-item-header a'))):
            title = soup.select('h3.lister-item-header a')[i].get_text()
            plot = soup.select('p.text-muted')[2 * i + 1].get_text()
            raw_list.append([title, mpa, plot])

crawl('G')

crawl('PG')

crawl('PG-13')

crawl('R')

raw_data = pd.DataFrame(raw_list, columns = ['Title', 'MPA', 'Plot'])
raw_data.Plot = raw_data.Plot.apply(lambda p: p.replace('\n', ''))
raw_data.head()

if not os.path.isdir(base_dir + 'data/'):
    os.mkdir(base_dir + 'data/')

if not os.path.isdir(base_dir + 'data/raw/'):
    os.mkdir(base_dir + 'data/raw/')

raw_data.to_csv(base_dir + 'data/raw/data.csv')

