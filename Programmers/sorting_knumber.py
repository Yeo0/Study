#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:46:16 2018

@author: yeoyoung
"""

# 문제 설명
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.

# 입출력 예
# array   commands    return
# [1, 5, 2, 6, 3, 7, 4]   [[2, 5, 3], [4, 4, 1], [1, 7, 3]]   [5, 6, 3]

# 입출력 예 설명
# [1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
# [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
# [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.


################################

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

##최적 솔루션
#파이썬에선 for 문에 한번에 여러개 변수 돌릴 수 있음
def solution(array, commands):
	answer=[]

	for i, j, k in commands:
		answer.append(sorted(array[i-1:j])[k-1])
		
	return answer



