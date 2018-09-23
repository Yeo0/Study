#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:46:16 2018

@author: yeoyoung
"""

# 세가지 과정을 통해 자르고 정렬하고 하라는거 뽑으면됨
# 1) array=[]
# 2) command 는 [i,j,k]모음
# 3) command 해서 나온 결과 값이 답
#command 의 개수는 제한없음


def solution(array,commands):
    answer=[]
    for list in commands:
        start=list[0]
        last=list[1] #5
        
        new_array=array[start-1:last]
        new_array.sort()
        
        k=list[2]
        ans=new_array[k-1]
        answer.append(ans)
     
    return answer

solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])
#return 값이 5,6,3 되어야
#command 값은 제한없음

# list=[[2,5,3],[4,4,1],[1,7,3]]
# list[0][0:2]
# print(list[0][0])
# print(len(list))