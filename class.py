import numpy as np
import pandas as pd
import seaborn as sns
import requests
import json
import time
import csv

f = open('tmdb_api.json')
api_key = json.load(f)
url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}'

"""
ids = []
discover = []
random = np.random.uniform(0, 0.1, 501)

for i in range(1, 501):
    params = {#'vote_count.gte': 1,
             #'sort_by': 'vote_count.desc', 
             'page': i,
             'primary_release_year': 2019,
             'language': 'en-US',
             'include_adult': 'false',
             'include_video': 'false'}
    response = requests.get(url, params)
    d = response.json()
    discover.extend(d['results'])
    ids.extend([d['results'][j]['id'] for j in range(len(d['results']))])
    time.sleep(random[i])

df = pd.DataFrame(discover)
df.to_csv('data_TMDB/discover2019.csv')

np.savetxt('data_TMDB/ids.txt', ids)
"""

ids=np.genfromtxt('data_TMDB/ids.txt')

film = []
for i in ids:
    url = f'https://api.themoviedb.org/3/movie/{i}?api_key={api_key}'
    params = {'language': 'en-US'}
    response = requests.get(url, params)
    film.append(response.json())
    time.sleep(np.random.uniform(0.5, 1))

df = pd.DataFrame(film)
df.to_csv('data_TMDB/movie2019.csv')
