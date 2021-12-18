# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 09:10:39 2021

@author: kevmm
"""
def Cum_sum(l):
   list1 = []
   cumsum = 0
   for element in l:
      cumsum += element
      list1.append(cumsum)
   return list1
lists = [5, 10, 20, 35, 50]
print ("list: ",Cum_sum(lists))