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

