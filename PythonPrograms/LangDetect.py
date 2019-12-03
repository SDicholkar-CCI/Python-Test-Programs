import langid as lng
from textblob import TextBlob
file = open("D:/Swapnil Data/spellAndGrammerCheck.txt", "rb")
sentence = file.read()
fileText = sentence.decode('utf-8')

for word in fileText.split(' '):
    b = TextBlob(word)
    print('TextBlo: ', word,  b.detect_language())
    """print(lng.classify(word))"""

