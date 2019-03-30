# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:11:48 2019

@author: Shivam-PC
"""

from cosineSimilarity import cosine_similar 

import pandas as pd
import numpy as np

def movieDB(plot, genre):
 
    
    movie_data = pd.read_csv("wiki_movie_plots_deduped.csv")
    movie_list=[]
    movie_details = dict()
     
    for row in movie_data.iterrows():
        movie_list.append([row[1][1],row[1][5],row[1][7]])
        
    for row in movie_list:
        if row[1] in genre:
            movie_details[row[0]] = cosine_similar(str(row[2]), plot)
        
    return movie_details
    
    

    