# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:11:48 2019

@author: Shivam-PC
"""
from cosineSimilarity import cosine_similar 

import pandas as pd
import numpy as np

def movieDB(plot):
    movie_data = pd.read_csv("wiki_movie_plots_deduped.csv")
    
    movie_details = dict()
    for row in movie_data.iterrows():
        movie_details[row[1][1]] = (cosine_similar(row[1][7], plot))
        
    return movie_details
    
    

    