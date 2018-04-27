# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:34:09 2018

@author: ram prasad
"""

import nltk
import random 
from nltk.corpus import movie_reviews 

documents =[(list(movie_reviews.words(fileid),category) 
             for category in movie_reviews.categories() 
             for fileid in movie_reviews.fileids(category))]

random.shuffle(documents)

#print(documents[0])

all_words =[]

for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words = nltk.FreqDist(all_words)

print(all_words.most_common(15))

print(all_words["stupid"])

words_features = list(all_words.keys())[:3000]

def find_features(documents):
    words = set(documents)
    features = {}
    for w in words_features:
        features[w] = (w in words)
    return features
print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
#features_sets = [(find_features(rev),category) for(rev,category) in documents]





