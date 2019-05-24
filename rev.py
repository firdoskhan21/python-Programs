# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:33:07 2019

@author: firdos
"""
def swap(x,y):
    return y,x

string1="Acd$er123#kjlbv?1@jbkk"
def check_alphanum(a):
     return a.isalnum()
str_List=[]
for i in string1:
    str_List.append(i)
    right_count=len(str_List)-1
    left_count=0
while left_count<right_count:
    if check_alphanum(str_List[left_count])!=1:
        left_count=left_count+1
    elif check_alphanum(str_List[right_count])!=1:
        right_count=right_count-1
    else:
        str_List[left_count] ,str_List[right_count]= swap(str_List[left_count],str_List[right_count])
        left_count =left_count+1
        right_count=right_count-1


reversed_str=''.join(str_List)
print string1
print reversed_str

