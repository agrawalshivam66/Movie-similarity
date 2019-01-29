# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:14:28 2019

@author: Shivam-PC
"""

import requests

#finding movie details entered by user
def movie(title):
    movieDetails = dict()
    moviePlot = ''
    movieGenre = ''
    
    try:
        # Make a get request to get movie details
        response = requests.get("http://www.omdbapi.com/?apikey=c6949711&t="+title)
        
        # get json response
        movieDetails = response.json()
        
        print(movieDetails['Plot'])
        moviePlot = movieDetails['Plot']
        movieGenre = movieDetails['Genre']
    
    except Exception as e:
        print("Movie not found")

    return moviePlot, movieGenre