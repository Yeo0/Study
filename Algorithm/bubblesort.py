# import random

# A=[i for i in range(1,1001)]
# #B=list(range(1,1001))

# #A=random.shuffle(A)
# print(B)



#Bubble sort
import numpy as np

# A=np.arange(1,1001)
# np.random.shuffle(A)
# # print(A) # input A
# # print(len(A))
# # for start in range(len(A)):
# # 	for i in range(1,len(A)-start):
# # 		if A[i-1]>A[i]:
# # 			temp=A[i-1]
# # 			A[i-1]=A[i]
# # 			A[i]=temp
# # print(A)


def Bubblesort(x):
	for start in range(len(x)):
		for i in range(1,len(x)-start):
			if x[i-1]>x[i]:
				temp=x[i-1]
				x[i-1]=x[i]
				x[i]=temp
	return x


A=np.arange(1,1001)
np.random.shuffle(A)

print(Bubblesort(A))

