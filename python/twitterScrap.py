import nltk
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union

url = "https://twitter.com/AirbnbHelp?lang=en"
urlclient = uReq(url)
page_html = urlclient.read()
urlclient.close()

page_soup = soup(page_html, "html.parser")


streamClass = page_soup.findAll("div", {"class":"content"})
#print(len(streamClass))

#srapping tweets

tweets = []

for content in streamClass:
	tweetContainer = content.find("div",{"class":"js-tweet-text-container"})
	tweet = tweetContainer.p.text
	#footerContainter = content.find("div",{"class":"stream-item-footer"})
	#reply = footerContainter.div.find("span",{"id":"profile-tweet-action-reply-count-aria-878063262486548480"}).text
	#print(tweet)
	tweets.append(tweet)

#tokenize words

words = word_tokenize(tweets[0])
#print(words)


#filtering stop words
stop_words = set(stopwords.words("english")) # it will consider the english stop words
filtered_sent = []

for w in words:
	if w not in stop_words:
		filtered_sent.append(w)

#print(filtered_sent)


#Stemming words

ps = PorterStemmer()
stemmed_word = []
for f in filtered_sent:
	stemmed_word.append(ps.stem(f))


#print(stemmed_word)


#Speech Tagging - define all word with appropriate verb, adjective, etc



#train_text = state_union.raw("tweets[0]")
#sample_text = state_union.raw("tweets[1]")

cust_tokenizer = PunktSentenceTokenizer(tweets[0])

tokenized = cust_tokenizer.tokenize(tweets[1])

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)

	except Exception as e:
		print(str(e))

process_content()

#Data Chunking - create chunks of different data types depends on speech tagging

def chunk_content():
	try:
		for j in tokenized:
			words = nltk.word_tokenize(j)
			tagged = nltk.pos_tag(words)
			
			chunkGram = r"""Chunk: {<NN.?>*<VB.?>*}"""

			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			chunked.draw()

	except Exception as e:
		print(str(e))

chunk_content()
