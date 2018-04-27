from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Ram Prasad , how are you today? how was the day"

print(sent_tokenize(example_text))
words_only = word_tokenize(example_text)

for i in words_only:
    print(i)
