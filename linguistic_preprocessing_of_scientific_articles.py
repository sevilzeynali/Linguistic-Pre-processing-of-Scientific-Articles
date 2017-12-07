#!/usr/bin/env python
# -*- coding: utf-8 -*-
#It is a program for pre-processing of the scientific articles before processing classification or keywords extraction or the other processing

#1.tokenisation 2.mettre en minuscule 3.lemmatization 4. enlever les mots qui sont dans le stop word 
import nltk
from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
import sys
reload(sys)

INPUT_FILE_PATH=""
OUTPUT_FILE_PATH=""

liste_of_liste_of_tokens=[]
sys.setdefaultencoding('utf-8')
#charging input file
fileIn=open(INPUT_FILE_PATH,"r")
#charging output files
fileOut=open(OUTPUT_FILE_PATH,"w")
#charging stop-word
stop_words=set(stopwords.words("english"))
#charging lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#read my input file: each document in one line
file = [line.decode('utf-8',errors='ignore').strip() for line in fileIn.readlines()]
#tokenisation
for liste in file:
    tokens= nltk.word_tokenize(liste)
    small_liste_of_tokens=[w.lower() for w in tokens]
    liste_of_liste_of_tokens.append(small_liste_of_tokens)
#lemmatizing
liste_of_lemmatized_tok=[]
for liste_of_toks in liste_of_liste_of_tokens:
    token_lemmatized=[wordnet_lemmatizer.lemmatize(x) for x in liste_of_toks]
    liste_of_lemmatized_tok.append(token_lemmatized)
#remove the tokens who exists in stop-word
for lemmes in liste_of_lemmatized_tok:
    for lemme in lemmes:
        if lemme in stop_words:
            lemmes.remove(lemme)
#write results in a txt file
for small_liste_of_lemmes in liste_of_lemmatized_tok:
    liste_to_string=' '.join(e for e in small_liste_of_lemmes)
    fileOut.write(liste_to_string)
    fileOut.write("\n")










    









    








       
   

    
    
    
    
    
    
    
    
    
    
    
    
    



    


 
