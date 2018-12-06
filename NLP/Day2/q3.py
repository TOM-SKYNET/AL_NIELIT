
#from textblob import Word
import textblob as tb

text = tb.TextBlob("Accept a sentence and display the parts of speech.")

for word, tag in text.tags:
    print word ,"=" , tag


