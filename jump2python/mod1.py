#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:12:29 2018
ip
@author: yeoyoung
"""

def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result=sum(a,b)
    return result

if __name__=="__main__": #함수만 불러올 때 / 파이썬 파일로 불러올 때 출력 안되게끔 하는 것
    print(sum(10,10.4))