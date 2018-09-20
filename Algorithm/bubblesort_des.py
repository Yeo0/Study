import numpy as np


def Bubblesort_des(x):
	for start in range(len(x)):
		for i in range(1,len(x)-start):
			if x[i-1]<x[i]:
				temp=x[i-1]
				x[i-1]=x[i]
				x[i]=temp
	return x



A=np.arange(1,1001)
np.random.shuffle(A)

print(Bubblesort_des(A))