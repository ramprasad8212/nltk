# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:34:09 2018

@author: ram prasad
"""

import nltk
import random 
from nltk.corpus import movie_reviews 

print(movie_reviews.words(fileid))

documents =[(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories() 
                 for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

print(documents[1])

all_words =[]

for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words = nltk.FreqDist(all_words)

#print(all_words.most_common(15))

#print(all_words["stupid"])

words_features = list(all_words.keys())[:3000]
test = "sridhar is the done the oas"

def find_features(documents):
    words = set(documents)
    features = {}
    for w in words_features:
        features[w] = (w in words)
    return features

#find_features(documents)
#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
featuresets = [(find_features(rev), category)  for(rev, category)  in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive - bayes algo accurecy percent:", nltk.classify.accuracy(classifier,testing_set)*100)


nltk.NaiveB
