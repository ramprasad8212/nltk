from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#nltk first program

example_sent="this is my new code for python ,which may help in automation"

words=word_tokenize(example_sent,language='english')

stop_words=set(stopwords.words("english"))

print(stop_words)
print(words)

