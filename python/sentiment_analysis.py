#pip install nltk

import nltk
#nltk.download()

# tokenizing - word and sentence tokenizers
# lexicon- words and their meaning 
# corporas - body of text - tweets


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords # eg: a,as, at, the, he, she, but, there etc


#for i in word_tokenize(text):
#	print(i)

text = "Hey, there?? How are you doing? Let's Party Tonight"
stop_words = set(stopwords.words("english")) # it will consider the english stop words
#print(stop_words) - to check what are the stop words!
#print(sent_tokenize(text)) # print the whole text in different sentences
#print(word_tokenize(text)) #it will make tokens of Text

words = word_tokenize(text)

filtered_sent = []

for w in words:
	if w not in stop_words:
		filtered_sent.append(w)
#print(stop_words)
print(filtered_sent)


