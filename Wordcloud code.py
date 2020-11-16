# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:09:19 2020

@author: Admin
"""

import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reader_ob= open("C:\\Users\\Admin\\Documents\\Data Science\\speech.txt")
type(reader_ob)
reader_contents = list(reader_ob)

text = ""



wordcloud = WordCloud(width=580, height=580, max_words=10).generate(text) 

# plot the WordCloud image  
#plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
#plt.axis("off") 
#plt.margins(x=0, y=0) 
plt.show() 
