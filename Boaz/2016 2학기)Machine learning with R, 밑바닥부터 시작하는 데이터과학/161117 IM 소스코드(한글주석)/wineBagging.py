#-*- coding: utf-8 -*-
__author__ = 'mike-bowles'

import urllib2
import numpy
import matplotlib.pyplot as plot
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from math import floor
import random


# UCI 웹 사이트에서 와인 품질 데이터 읽기
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
        #행을 float 형으로 변환
        floatRow = [float(num) for num in row]
        xList.append(floatRow)

nrows = len(xList)
ncols = len(xList[0])


#샘플의 30%로 고정 테스트 세트 구성
nSample = int(nrows * 0.30)
idxTest = random.sample(range(nrows), nSample)
idxTest.sort()
idxTrain = [idx for idx in range(nrows) if not(idx in idxTest)]

#속성과 레이블의 테스트 세트와 트레이닝 세트 정의
xTrain = [xList[r] for r in idxTrain]
xTest = [xList[r] for r in idxTest]
yTrain = [labels[r] for r in idxTrain]
yTest = [labels[r] for r in idxTest]

#트레이닝 데이터의 임의 부분 집합으로 일련의 모델 트레이닝
#리스트에 모델을 모으고, 리스트가 늘어남에 따라 복합 오차 체크

#생성할 모델의 최대 개수
numTreesMax = 100

#트리 깊이 - 일반적으로 최상층
treeDepth = 5

#모델을 담기 위해 리스트 초기화
modelList = []
predList = []

#확률 배깅을 위하여 추출할 샘플의 수
bagFract = 0.5
nBagSamples = int(len(xTrain) * bagFract)

for iTrees in range(numTreesMax):
    idxBag = []
    for i in range(nBagSamples):
        idxBag.append(random.choice(range(len(xTrain))))
    xTrainBag = [xTrain[i] for i in idxBag]
    yTrainBag = [yTrain[i] for i in idxBag]

    modelList.append(DecisionTreeRegressor(max_depth=treeDepth))
    modelList[-1].fit(xTrainBag, yTrainBag)

    #가장 최근 모델로 예측을 만들고 예측 리스트에 추가하기
    latestPrediction = modelList[-1].predict(xTest)
    predList.append(list(latestPrediction))


#최초 n개 모델에서 누적한 예측 생성
mse = []
allPredictions = []
for iModels in range(len(modelList)):

    #예측 중 처음 "iModels"개의 평균 구하기
    prediction = []
    for iPred in range(len(xTest)):
        prediction.append(sum([predList[i][iPred] for i in range(iModels + 1)])/(iModels + 1))

    allPredictions.append(prediction)
    errors = [(yTest[i] - prediction[i]) for i in range(len(yTest))]
    mse.append(sum([e * e for e in errors]) / len(yTest))

nModels = [i + 1 for i in range(len(modelList))]

plot.plot(nModels,mse)
plot.axis('tight')
plot.xlabel('Number of Models in Ensemble')
plot.ylabel('Mean Squared Error')
plot.ylim((0.0, max(mse)))
plot.show()

print('Minimum MSE')
print(min(mse))


#With treeDepth = 5
#     bagFract = 0.5
#Minimum MSE
#0.429310223079

#With treeDepth = 8
#     bagFract = 0.5
#Minimum MSE
#0.395838627928

#With treeDepth = 10
#     bagFract = 1.0
#Minimum MSE
#0.313120547589