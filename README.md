# Linguistic Pre-processing Of Scientific Articles

This is a program in Python for preprocessing the text before keyword extraction or classification or other processing. It uses Python [nltk](http://www.nltk.org/) library.

## Installing and requirements

You need Python >= 2.6 or >= 3.3

You must install nltk to use this program :

```
$ sudo pip install -U nltk

```

## How to use

The input file should contanins scientific articles in txt format. each line one document in this 

In output folder you will have the processed input file.

## preprocessings
This program dose :

1. tokenisation
2. put the text in lowercase
3. lemmatizing
4. remove the words existing in stop-word of nltk
