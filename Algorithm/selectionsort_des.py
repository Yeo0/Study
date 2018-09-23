N=int(input("배열 크기를 입력하세요: "))

inputlist=[]

for i in range(N):
	element = input("배열의 원소를 입력해 주세요: ")
	inputlist.append(element)


print(inputlist)

def Selectionsort_des(x):
	for i in range(len(x)-1):
		min=i
		for j in range(i+1,len(x)):	
			if x[j] > x[min]:
				min=j
		temp=x[i]
		x[i]=x[min]
		x[min]=temp
	return x



print(Selectionsort_des(inputlist))


