from textblob import TextBlob
from newspaper import Article
import nltk

def sentimentAnalysis():

    #nltk.download('punkt')     #Use this line if running on a fresh machine

    file = open("ex2.txt",'r')
    #file = open("example.txt","r")

    #print(file)
    text = str([word.encode('utf-8') for word in file])
    print(text)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment>0.5:
        return "Great Day"
    if sentiment>0:
        return "Good Day"
    if sentiment>-0.5:
        return "Bad Day"
    else:
        return "Terrible Day"
    

    #return(sentiment)   #varies from -1 to 1   negative to positive