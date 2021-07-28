"""

This document will collect my efforts at Natural Language Processing

"""
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.tree import Tree
from nltk.parse import api
from nltk.chat import iesha_chat
import nltk

from nltk.tokenize import WordPunctTokenizer


passage = input("Write a sentence: ")
passage = "(" + passage + ")"
print(sent_tokenize(passage))
words = word_tokenize(passage)
print(words)
tagged_words = pos_tag(words)
print(tagged_words)

#nltk.chunk.regexp.demo()

tree = Tree
t = tree.fromstring(passage)
#t.draw()


grammar1 = "NP: {<DT>?<JJ>*<NN>}"
grammer2 = "NP: {<NNP.?>*<NN.?>*<CD.?>*<NN.?>}"
parser1 = nltk.RegexpParser(grammar1)
parsed = parser1.parse(tagged_words)
print(parsed)
parsed.draw()
parser2 = nltk.RegexpParser(grammer2)
parsed = parser2.parse(tagged_words)
print(parsed)
parsed.draw()




