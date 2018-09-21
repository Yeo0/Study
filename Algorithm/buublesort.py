import random



def Bubblesort_asc(x):
	for start in range(len(x)):
		for i in range(1,len(x)-start):
			if x[i-1]>x[i]:
				temp=x[i-1]
				x[i-1]=x[i]
				x[i]=temp
	return x


A=list(range(1,1001))
random.shuffle(A)
print(Bubblesort_asc(A))
