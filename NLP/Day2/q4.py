
#from textblob import Word
import textblob as tb

fd = open("s.txt","r")
text = tb.TextBlob(fd.read())

print 'Title:', text.sentences[0]
print 'No. of sentences:', len(text.sentences)
print 'No. of Words:', len(text.words)
print 'Main Words\n'

for word, tag in text.tags:
    if tag == 'NN' or tag == 'NNS':
        print '--', word ,"=" , tag


fd.close()
