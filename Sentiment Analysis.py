# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 14:55:30 2016

@author: Mads
"""
# importing packages
import io, unicodedata
from afinn import Afinn

# importing file
filename ="konservativ_twitterfile.txt"

# setting encoding and reading
f = io.open(filename,'r',encoding='utf8')
text = f.read()
text = unicodedata.normalize('NFKD', text)

# splitting text into words
tweets = text.split("\n")
for text in tweets:
    # apply Afinn da 32
    afinn = Afinn(language='da')
    # getting the score
    afinn.score(text)
    # printing the score
    print afinn.score(text)