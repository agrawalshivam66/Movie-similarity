# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:04:34 2019

@author: Shivam-PC
"""
from cosineSimilarity import cosine_similar
from movieAPI import movie
from wiki_movie_plots_read import movieDB

title = str(input("Enter the movie name "))
moviePlot, movieGenre = movie(title)
movie_detail = movieDB(moviePlot)


