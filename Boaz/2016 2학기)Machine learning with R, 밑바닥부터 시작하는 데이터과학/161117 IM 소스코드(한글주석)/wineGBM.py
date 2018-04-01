#-*- coding: utf-8 -*-
import urllib2
import numpy
from sklearn.cross_validation import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
import pylab as plot

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

X = numpy.array(xList)
y = numpy.array(labels)
wineNames = numpy.array(names)

# 데이터 행의 30%로 고정된 세트 구성
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.30, random_state=531)

# 평균 제곱 오차를 최소화하는 그래디언트 부스팅 모델 트레이닝
nEst = 2000
depth = 7
learnRate = 0.01
subSamp = 0.5
wineGBMModel = ensemble.GradientBoostingRegressor(n_estimators=nEst,
                                                  max_depth=depth,
                                                  learning_rate=learnRate,
                                                  subsample = subSamp,
                                                  loss='ls')

wineGBMModel.fit(xTrain, yTrain)

# 테스트 세트로 MSE 계산하기
msError = []
predictions = wineGBMModel.staged_predict(xTest)
for p in predictions:
    msError.append(mean_squared_error(yTest, p))

print("MSE" )
print(min(msError))
print(msError.index(min(msError)))

# 트레이닝과 테스트 오차 대비 앙상블의 트리 개수 도표 그리기
plot.figure()
plot.plot(range(1, nEst + 1), wineGBMModel.train_score_, label='Training Set MSE')
plot.plot(range(1, nEst + 1), msError, label='Test Set MSE')
plot.legend(loc='upper right')
plot.xlabel('Number of Trees in Ensemble')
plot.ylabel('Mean Squared Error')
plot.show()

# 피처 중요도 도표 그리기
featureImportance = wineGBMModel.feature_importances_

# 가장 높은 중요도로 정규화
featureImportance = featureImportance / featureImportance.max()
idxSorted = numpy.argsort(featureImportance)
barPos = numpy.arange(idxSorted.shape[0]) + .5
plot.barh(barPos, featureImportance[idxSorted], align='center')
plot.yticks(barPos, wineNames[idxSorted])
plot.xlabel('Variable Importance')
plot.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)
plot.show()


# Printed Output:
# for:
#nEst = 2000
#depth = 7
#learnRate = 0.01
#subSamp = 0.5
#
# MSE
# 0.313361215728
# 840
