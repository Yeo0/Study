#-*- coding: utf-8 -*-
__author__ = 'mike-bowles'

import urllib2
import numpy
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.externals.six import StringIO
from math import sqrt
import matplotlib.pyplot as plot

#데이터를 읽은 후 반복 수행
target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = urllib2.urlopen(target_url)

xList = []
labels = []
names = []
firstLine = True
for line in data:
    if firstLine:
        names = line.strip().split(";")
        firstLine = False
    else:
        #세미콜론으로 분리
        row = line.strip().split(";")
        #레이블을 다른 어레이로 넣기
        labels.append(float(row[-1]))
        #행에서 레이블 제거
        row.pop()
        #행을 float형으로 변환
        floatRow = [float(num) for num in row]
        xList.append(floatRow)

nrows = len(xList)
ncols = len(xList[0])

wineTree = DecisionTreeRegressor(max_depth=3)

wineTree.fit(xList, labels)

#wineTree.doc으로 익스포트
with open("wineTree.dot", 'w') as f:
    f = tree.export_graphviz(wineTree, out_file=f)

