# -*- coding: utf-8 -*-
"""Exp3 RS 60017220097

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SHUxd9tErRUhmbiz8xTJeTN_7EaLF4aL
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('netflix_titles.csv')
# Replace NaN with an empty string
df['description'] = df['description'].fillna('')

df.head()

# Create a TfidfVectorizer and Remove stopwords
tfidf = TfidfVectorizer(stop_words='english')
# Fit and transform the data to a tfidf matrix
tfidf_matrix = tfidf.fit_transform(df['description'])
# Print the shape of the tfidf_matrix
tfidf_matrix.shape

# Compute the cosine similarity between each movie description
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

cosine_sim

indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim, num_recommend = 10):
    idx = indices[title]
# Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
# Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# Get the scores of the 10 most similar movies
    top_similar = sim_scores[1:num_recommend+1]
# Get the movie indices
    movie_indices = [i[0] for i in top_similar]
# Return the top 10 most similar movies
    return df['title'].iloc[movie_indices]

get_recommendations('Power Rangers Zeo', num_recommend = 20)

#Dick Johnson Is Dead
get_recommendations('Dick Johnson Is Dead', num_recommend = 20)

get_recommendations('Kota Factory', num_recommend = 20)

get_recommendations('Drishyam', num_recommend = 20)

get_recommendations('End Game', num_recommend = 20)

