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
genreList=movieGenre.split(', ')
for i in range(len(genreList)):
    genreList[i]=genreList[i].lower()

#getting cosine similarity values    
movie_detail = movieDB(moviePlot,genreList )
#Sorting
movie_detail = sorted(movie_detail.items(), key=lambda kv: kv[1])