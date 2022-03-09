# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:01:12 2022

@author: Pc
"""

def reverse(sentence, reverse_word) :
  words=sentence.split()
  if (isinstance(reverse_word, str)==False):
      return("invalid input")
  val='The word was not found'
  for word in words:
      if word==reverse_word:
          val=word[::-1]
          break
  return val

