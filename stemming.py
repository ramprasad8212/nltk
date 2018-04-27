from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

PS = PorterStemmer()

##ex_word = ["python","pythonli","pythoner","pythoning","pythonly"]

##for w in ex_word:
##    print(PS.stem(w))


new_text = "this very good example for stemming , all stems going to come uder out stemed words for stemerization . all the best for stemly work"

words = word_tokenize(new_text)

for i in words:
    print(PS.stem(i))
