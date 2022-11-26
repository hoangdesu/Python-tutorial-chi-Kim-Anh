#Le Thi Ngoc Tho
# 3/2018
#Doan code nay demo cho sinh vien ve phuong phap tom tat van ban bang phan lop

import nltk
import string
import os
import numpy as np
from collections import Counter
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.tag import pos_tag

# Pre-process DUC data

def termFreq(doc):        
    word_tokens = doc.split(" ")
    tf = Counter(word_tokens)
    return tf

#def freq(word, doc):
    #return doc.count(word)

def docFreq(word, doclist):
    doccount = 0
    for doc in doclist:
        if doc.count(word) > 0:
            doccount +=1
    return doccount 

def idf(wordlist, doclist):
    idfList = []
    N = len(doclist)
    for word in wordlist: 
        df = docFreq(word, doclist)
        idf = np.log(N/(1+df));
        word_idf = (word, idf)
        idfList.append(word_idf)
    return idfList

#my_idf_vector = [idf(word, mydoclist) for word in vocabulary]

def get_tokens(filePath):
    with open(filePath, 'r') as ducTxt:
        text = ducTxt.read()
        #print(text)
        lowers = text.lower()
        #remove the punctuation using the character deletion step of translate
        no_punctuation = lowers.translate(string.punctuation)
        tokens = nltk.word_tokenize(no_punctuation)
        return tokens

#def stem_tokens(tokens, stemmer):
    #stemmed = []
    #for item in tokens:
        #stemmed.append(stemmer.stem(item))
    #return stemmed

#def tokenize(text, stemmer):
    #tokens = nltk.word_tokenize(text)
    #stems = stem_tokens(tokens, stemmer)
    #return stems

def getIDF(corpus):
    # Read all documents and all words in corpus for IDF
    stemmer = PorterStemmer()
    doclist = []
    wordlist = []
    for docFile in os.listdir(corpusPath):
        docFilePath = corpusPath + docFile
        with open(docFilePath, 'r') as myfile:
            docText = myfile.read().lower().translate(string.punctuation)
            tokens = nltk.word_tokenize(docText)
            stemmed = []
            stemmedDoc = ""
            for item in tokens:
                stem = stemmer.stem(item)
                stemmedDoc += stem + " "
                try: # Find index of a stem word, if it is not in list, add it to word list
                    idx = wordlist.index(stem)
                except ValueError:
                    wordlist.append(stem)
            doclist.append(stemmedDoc)
    idfList = idf(wordlist, doclist)
    return idfList

def stemDocText(docText, stemmer):
    tokens = nltk.word_tokenize(docText)
    wordlist = []
    stemmedDoc = ""
    for item in tokens:
        stem = stemmer.stem(item)
        stemmedDoc += stem + " "
        try: # Find index of a stem word, if it is not in list, add it to word list
            idx = wordlist.index(stem)
        except ValueError:
            wordlist.append(stem)
    return (wordlist, stemmedDoc)

# Check if a given sentence contain indicator word of summarization
def containIndicatorWord(sentence):
    contain = 0
    indicatorWord = ['finally', 'in a word', 'in brief', 'briefly', 'in conclusion', \
                     'in the end', 'in the final analysis', 'on the whole', 'thus', \
                     'to conclude', 'to summarize', 'in sum', 'to sum up', 'in summary']
    for w in indicatorWord:
        if w in sentence:
            contain = 1
            break
    return contain

def extractFeatureVector(document, lblSentences, stemmer):
    # Get clean text for frequencies
    cleanText = ""
    sentences = document.rstrip().split('\n')
    for s in sentences:
        bgn = s.index('">')
        end = s.index('</s>')
        sTxt = s[bgn:end]
        cleanText += sTxt + "\n"
    docTxt = cleanText.lower().translate(string.punctuation)
    wordList, stemmedDoc = stemDocText(cleanText, stemmer)
    tf = termFreq(stemmedDoc)
    #print(tf)
    common = [word for word, freq in tf.most_common(10)] # Print the most common word to debug. Note that, stopwords are not eliminated
    #print(common)
    
    sentCount = 0
    numSentences = len(sentences)
    for sent in sentences:
        f1 = f2 = f3 = f4 = f5 = f6 = 0 
        sentCount = sentCount + 1
        try:
            b = sent.index('wdcount=') + 9
            e = sent.index('>') - 1   
            wdcount = int(sent[b:e])
            if(wdcount > 10):
                f1 = 1
        except ValueError as e:
            print(e)
        try:
            bgn = sent.index('\">') + 2
            end = sent.index('</s>')
            cleanSent = sent[bgn:end].rstrip()
            f2 = containIndicatorWord(cleanSent)
        except ValueError as e:
            print(e)
        if(sentCount == 1):
            f3 = 1
        elif(sentCount == numSentences):
            f3 = 3
        else:
            f3 = 2
        # Check if sentence contain frequent words
        for cw in common:
            if(cw in cleanSent):
                f4 = 1
                break
        # Check if sentence contain proper noun
        tagged_sent = pos_tag(cleanSent.split())
        #print(tagged_sent)
        propernouns = [wrd for wrd, pos in tagged_sent if pos == 'NNP']
        if(len(propernouns) > 2):
            f5 = 1
        if(sent in lblSentences):
            f6 = 1
            print("SUMMARY SENTENCE HERE ........................")
        vec = (f1, f2, f3, f4, f5, f6)
        print(vec)
        
    return
        
def main():
    cwd = os.getcwd()
    DUC_TEXT = cwd + "\\DUC_TEXT"
    DUC_SUM = cwd + "\\DUC_SUM"
    corpusPath = cwd + "\\corpus\\"
    
    #idfList = getIDF(corpus)
    
    stemmer = PorterStemmer()
    # Create train file
    trainDir = DUC_TEXT + "\\train\\"
    for docFile in os.listdir(trainDir):
        docFilePath = trainDir + docFile
        labelFilePath = DUC_SUM + "\\" + docFile
        #print(docFile)
        with open(labelFilePath, 'r') as lbl, open(docFilePath, 'r') as txt:
            txtContents = txt.read().rstrip()
            txtSentences = txtContents.split('\n')
            lblSentences = lbl.read().split('\n')
            aDocument = ""
            prevDocId = ""
            for sent in txtSentences:
                # Get the information
                #print(sent)
                try:
                    bgn = sent.index('docid=') + 7
                    end = sent.index('num=') - 2
                    docid = sent[bgn:end]
                    if(prevDocId == ""):
                        prevDocId = docid
                    if(docid == prevDocId):
                        aDocument += sent + '\n'
                    else:
                        prevDocId = docid
                        aDocument = aDocument.rstrip()
                        extractFeatureVector(aDocument, lblSentences, stemmer)
                        aDocument = sent + '\n' 
                except ValueError as e:
                    print('Msg by Tho: Error at ' + sent)
                    print(e)
    
    # Create test file
    
    
    return

trainSammples = main()
print(type(trainSammples))

from sklearn.neural_network import MLPRegressor

print(trainSammples)
X = trainSammples[1:5]
print(type(X))
y = trainSammples[6]
print(type(y))
clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)
Z = [[2., 2.], [-1., -2.]]
print(type(Z))
t = testData.tolist()
print('type of t', type(t))
a = clf.predict(t)
print('RESULTS:')
for r in a:
    print(r)