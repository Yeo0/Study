__author__ = 'mike-bowles'

import numpy
import matplotlib.pyplot as plot
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.externals.six import StringIO

# y = x + �������� ������ ������ ��Ʈ �����ϱ�
nPoints = 100

# ��ǥ�� �׸� x ��
xPlot = [(float(i)/float(nPoints) - 0.5) for i in range(nPoints + 1)]

# x�� ����Ʈ�� ����Ʈ��
x = [[s] for s in xPlot]

# y(���̺�)���� x���� �߰��� ������ ����� �ִ�
# �õ� ����
numpy.random.seed(1)
y = [s + numpy.random.normal(scale=0.1) for s in xPlot]

nrow = len(x)

# ���̿� ���� ���� �� ������ Ʈ���� �����ϰ�, � ���� �������� Ȯ���ϱ� ���Ͽ� ���� ���� ����ϱ�

depthList = [1, 2, 3, 4, 5, 6, 7]
xvalMSE = []
nxval = 10

for iDepth in depthList:

    # Ʈ���� �����ϱ� ���� ���� ���� ������ ����� ǥ�� �� �����ͷ� ���ϱ�
    for ixval in range(nxval):

        # �׽�Ʈ �ε��� ��Ʈ�� Ʈ���̴� �ε��� ��Ʈ ����
        idxTest = [a for a in range(nrow) if a%nxval == ixval%nxval]
        idxTrain = [a for a in range(nrow) if a%nxval != ixval%nxval]

        # �Ӽ��� ���̺��� �׽�Ʈ ��Ʈ�� Ʈ���̴� ��Ʈ ����
        xTrain = [x[r] for r in idxTrain]
        xTest = [x[r] for r in idxTest]
        yTrain = [y[r] for r in idxTrain]
        yTest = [y[r] for r in idxTest]

        # ������ ������ Ʈ���� Ʈ���̴��ϰ� ǥ�� �� (OOS) ������ �����ϱ�
        treeModel = DecisionTreeRegressor(max_depth=iDepth)
        treeModel.fit(xTrain, yTrain)

        treePrediction = treeModel.predict(xTest)
        error = [yTest[r] - treePrediction[r] for r in range(len(yTest))]

        # �����ϱ�
        if ixval == 0:
            oosErrors = sum([e * e for e in error])
        else:
            # ���� ���� �����ϱ�
            oosErrors += sum([e * e for e in error])

    # ���� ���� ����� ���ϰ� Ʈ�� ���̿� ���� �����ϱ�

    mse = oosErrors/nrow
    xvalMSE.append(mse)

plot.plot(depthList, xvalMSE)
plot.axis('tight')
plot.xlabel('Tree Depth')
plot.ylabel('Mean Squared Error')
plot.show()