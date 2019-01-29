# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:04:34 2019

@author: Shivam-PC
"""
from cosineSimilarity import cosine_similar
from movieAPI import movie

title = str(input("Enter the movie name "))
moviePlot, movieGenre = movie(title)

cosine_similar(moviePlot, 'the movie is based on this')