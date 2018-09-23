N=int(input())

inputlist=[]

for i in range(N):
	element = input()
	inputlist.append(element)

def Bubblesort_asc(x):
	for start in range(len(x)):
		for i in range(1,len(x)-start):
			if x[i-1]>x[i]:
				temp=x[i-1]
				x[i-1]=x[i]
				x[i]=temp
	return x


for list in Bubblesort_asc(inputlist):
    print(list)
