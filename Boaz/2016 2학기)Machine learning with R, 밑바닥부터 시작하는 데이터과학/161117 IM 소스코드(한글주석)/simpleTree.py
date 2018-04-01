#-*- coding: utf-8 -*-
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

# x를 리스트의 리스트로 만들어야 한다
x = [[s] for s in xPlot]

# y(레이블)에는 x 값에 추가학 무작위 노이즈가 있다
# 시드 설정
numpy.random.seed(1)
y = [s + numpy.random.normal(scale=0.1) for s in xPlot]

plot.plot(xPlot,y)
plot.axis('tight')
plot.xlabel('x')
plot.ylabel('y')
plot.show()

simpleTree = DecisionTreeRegressor(max_depth=1)
simpleTree.fit(x, y)

# 트리 그리기
with open("simpleTree.dot", 'w') as f:
    f = tree.export_graphviz(simpleTree, out_file=f)

# 실제 값과 트리의 예측 비교
yHat  = simpleTree.predict(x)

plot.figure()
plot.plot(xPlot, y, label='True y')
plot.plot(xPlot, yHat, label='Tree Prediction ', linestyle='--')
plot.legend(bbox_to_anchor=(1,0.2))
plot.axis('tight')
plot.xlabel('x')
plot.ylabel('y')
plot.show()

simpleTree2 = DecisionTreeRegressor(max_depth=2)
simpleTree2.fit(x, y)

# 트리 export
with open("simpleTree2.dot", 'w') as f:
    f = tree.export_graphviz(simpleTree2, out_file=f)

# 실제 값과 트리의 예측 비교

yHat  = simpleTree2.predict(x)

plot.figure()
plot.plot(xPlot, y, label='True y')
plot.plot(xPlot, yHat, label='Tree Prediction ', linestyle='--')
plot.legend(bbox_to_anchor=(1,0.2))
plot.axis('tight')
plot.xlabel('x')
plot.ylabel('y')
plot.show()

# 분기점 계산 - 최적 분기점을 찾기 위하여 모든 가능한 분기점을 사용함
sse = []
xMin = []
for i in range(1, len(xPlot)):
    # 리스트를 분기점의 왼쪽과 오른쪽으로 나누기
    lhList = list(xPlot[0:i])
    rhList = list(xPlot[i:len(xPlot)])

    # 각각의 평균 계산
    lhAvg = sum(lhList) / len(lhList)
    rhAvg = sum(rhList) / len(rhList)

    # 왼쪽, 오른쪽, 전체의 오차 제곱합 계산
    lhSse = sum([(s - lhAvg) * (s - lhAvg) for s in lhList])
    rhSse = sum([(s - rhAvg) * (s - rhAvg) for s in rhList])

    # 왼쪽과 오른쪽의 합계를 오차 리스트에 추가

    sse.append(lhSse + rhSse)
    xMin.append(max(lhList))

plot.plot(range(1, len(xPlot)), sse)
plot.xlabel('Split Point Index')
plot.ylabel('Sum Squared Error')
plot.show()

minSse = min(sse)
idxMin = sse.index(minSse)
print(xMin[idxMin])


simpleTree6 = DecisionTreeRegressor(max_depth=6)
simpleTree6.fit(x, y)

#too many nodes to draw the tree
#with open("simpleTree2.dot", 'w') as f:
#    f = tree.export_graphviz(simpleTree6, out_file=f)

# 실제 값과 트리 예측 비교

yHat  = simpleTree6.predict(x)

plot.figure()
plot.plot(xPlot, y, label='True y')
plot.plot(xPlot, yHat, label='Tree Prediction ', linestyle='--')
plot.legend(bbox_to_anchor=(1,0.2))
plot.axis('tight')
plot.xlabel('x')
plot.ylabel('y')
plot.show()

