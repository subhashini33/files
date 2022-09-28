import nltk # nltk.word_tokenize
from nltk import * # all
from nltk import word_tokenize

f = open("sample.txt", "r",encoding="utf8")

raw = f.read()
res = word_tokenize(raw)
print(res)
f.close()