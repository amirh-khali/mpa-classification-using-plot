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

# **Data Collection**

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

# **Preprocessing**

df = pd.read_csv(base_dir + 'data/raw/data.csv', index_col=0)
df

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

df = df.drop(df[df.Plot == 'Add a Plot'].index)
df = df.reset_index().drop(columns = 'index')
df['Plot'] = df['Plot'].str.replace('See full summary', '')

df['Normalized_Plot'] = df['Plot'].str.lower()
df['Normalized_Plot'] = df['Normalized_Plot'].str.translate(str.maketrans('', '', string.punctuation + '»' + '«'))
df['Normalized_Plot'] = df['Normalized_Plot'].str.translate(str.maketrans('', '', string.digits))
df['Normalized_Plot'] = df['Normalized_Plot'].apply(word_tokenize)
df['Normalized_Plot'] = df['Normalized_Plot'].apply(lambda lst : [word for word in lst if word not in set(stopwords.words('english'))])
df['Normalized_Plot'] = df['Normalized_Plot'].apply(lambda lst : [WordNetLemmatizer().lemmatize(w) for w in lst])

if not os.path.isdir(base_dir + 'data/'):
    os.mkdir(base_dir + 'data/')

if not os.path.isdir(base_dir + 'data/cleaned/'):
    os.mkdir(base_dir + 'data/cleaned/')

df.to_csv(base_dir + 'data/cleaned/data.csv')

# **Stats**

df = pd.read_csv(base_dir + 'data/cleaned/data.csv', index_col=0)
df

MPA_counts = {MPA : sum(df['MPA'] == MPA) for MPA in ['G', 'PG', 'PG-13', 'R']}
plt.bar(MPA_counts.keys(), MPA_counts.values())
plt.show()

counter = Counter()
df['Normalized_Plot'].apply(lambda lst : ast.literal_eval(lst)).apply(counter.update)

counter_list = [(k, v) for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)]
counter_list = counter_list[:10]
x, y = zip(*counter_list)
plt.figure(figsize=(10, 5), facecolor=None)
plt.bar(x, y)
plt.show()

print('Sentence count:', df['Plot'].apply(sent_tokenize).apply(len).sum())
print('All words(preprocessed words):', sum(counter.values()))
print('Unique words:', len(counter))

