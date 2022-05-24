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

