# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:22:28 2019

@author: Shivam-PC
"""
import math

def cosine_similar(s1, s2):
    word1 = s1.split()
    word2 = s2.split()
    
    line1 = dict()
    line2 = dict()
    
    for i in word1:
        line1[i] = word1.count(i)        
    
    for i in word2:
        line2[i] = word2.count(i)
    
    intersection = set(line1.keys()) & set(line2.keys())
        
    numerator = 0
    for x in intersection:
        numerator += line1[x] * line2[x]
    
    sum1 = 0
    sum2 = 0
    for i in line1.keys():
        sum1 += line1[i]**2
    
    for i in line2.keys():
        sum2 += line2[i]**2
    
    denominator = math.sqrt(sum1) + math.sqrt(sum2)
    
    cosine_value = float(numerator) / denominator
      
    return cosine_value     


s1 = 'the game of a life is a game of everlasting learning'
s2 = 'the unexamined life is not worth living'

cosine_value = cosine_similar(s1, s2)
print(cosine_value)

