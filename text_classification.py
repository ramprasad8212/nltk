# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:36:57 2018

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


