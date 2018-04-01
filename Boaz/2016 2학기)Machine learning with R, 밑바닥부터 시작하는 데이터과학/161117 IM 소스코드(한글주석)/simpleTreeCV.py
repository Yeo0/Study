__author__ = 'mike-bowles'

import numpy
import matplotlib.pyplot as plot
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.externals.six import StringIO

# y = x + 랜덤으로 간단한 데이터 세트 생성하기
nPoints = 100

# 도표로 그릴 x 값
xPlot = [(float(i)/float(nPoints) - 0.5) for i in range(nPoints + 1)]

# x를 리스트의 리스트로
x = [[s] for s in xPlot]

# y(레이블)에는 x값에 추가한 무작위 노이즈가 있다
# 시드 설정
numpy.random.seed(1)
y = [s + numpy.random.normal(scale=0.1) for s in xPlot]

nrow = len(x)

# 깊이에 대한 여러 개 값으로 트리를 적합하고, 어떤 값이 최적인지 확인하기 위하여 교차 검증 사용하기

depthList = [1, 2, 3, 4, 5, 6, 7]
xvalMSE = []
nxval = 10

for iDepth in depthList:

    # 트리를 적합하기 위한 교차 검정 루프를 만들고 표본 외 데이터로 평가하기
    for ixval in range(nxval):

        # 테스트 인덱스 세트와 트레이닝 인덱스 세트 정의
        idxTest = [a for a in range(nrow) if a%nxval == ixval%nxval]
        idxTrain = [a for a in range(nrow) if a%nxval != ixval%nxval]

        # 속성과 레이블의 테스트 세트와 트레이닝 세트 정의
        xTrain = [x[r] for r in idxTrain]
        xTest = [x[r] for r in idxTest]
        yTrain = [y[r] for r in idxTrain]
        yTest = [y[r] for r in idxTest]

        # 적절한 깊이인 트리를 트레이닝하고 표본 외 (OOS) 오차를 누적하기
        treeModel = DecisionTreeRegressor(max_depth=iDepth)
        treeModel.fit(xTrain, yTrain)

        treePrediction = treeModel.predict(xTest)
        error = [yTest[r] - treePrediction[r] for r in range(len(yTest))]

        # 누적하기
        if ixval == 0:
            oosErrors = sum([e * e for e in error])
        else:
            # 제곱 오차 누적하기
            oosErrors += sum([e * e for e in error])

    # 제곱 오차 평균을 구하고 트리 깊이에 따라 누적하기

    mse = oosErrors/nrow
    xvalMSE.append(mse)

plot.plot(depthList, xvalMSE)
plot.axis('tight')
plot.xlabel('Tree Depth')
plot.ylabel('Mean Squared Error')
plot.show()