import nltk
import numpy
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import nltk.numpy

##train_text  =  state_union.raw("2005-GWBush.txt")
sample_text =  state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)
print(custom_sent_tokenizer)

tokenized = custom_sent_tokenizer.tokenize(sample_text)
print(tokenized)

def process_content():
    try:
        for i in tokenized:
            words= nltk.word_tokenize(i)
##            print(words)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""ramprasad:{<RB.?>*<VB.?>}"""
            
            chunkParser= nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            named_ent = nltk.ne_chunk(tagged)
            named_ent.draw()
##            chunked.draw()
##            print(chunked)
##            print(tagged)
    except exception as e :
            print(str(e))



process_content()
##print(words)

namedEnt = nltk.ne_chunk(tagged)
namedEnt.draw()

            
