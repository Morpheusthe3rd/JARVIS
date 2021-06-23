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


passage = input("Write a sentence")

print(sent_tokenize(passage))
print(word_tokenize(passage))
parser = nltk.chunk.regexp.RegexpChunkParser(nltk.chunk.regexp.ChunkRule, trace=0)
tree = Tree
t = tree.fromstring(passage)
t.draw()
print(parser.parse(pos_tag(word_tokenize(passage))))



