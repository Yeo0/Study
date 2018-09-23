N=int(input("배열 크기를 입력하세요: "))

inputlist=[]

for i in range(N):
	element = input("배열의 원소를 입력해 주세요: ")
	inputlist.append(element)


print(inputlist)


def Bubblesort_asc(x):
	for start in range(len(x)):
		for i in range(1,len(x)-start):
			if x[i-1]<x[i]:
				temp=x[i-1]
				x[i-1]=x[i]
				x[i]=temp
	return x

print(Bubblesort_asc(inputlist))