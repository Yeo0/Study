#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:57:14 2018

@author: yeoyoung
"""

PI=3.141592

class Math:
    def solv(self,r):
        return PI*(r**2)
    
def sum(a,b):
    return a+b

if __name__=="__main__":
    print(PI)
    a=Math()
    print(a.solv(2))
    print(sum(PI, 4.4))