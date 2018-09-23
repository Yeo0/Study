N=int(input("배열 크기를 입력하세요: "))

inputlist=[]

for i in range(N):
	element = input("배열의 원소를 입력해 주세요: ")
	inputlist.append(element)


print(inputlist)

def Insertionsort_asc(x):
	for i in range(len(x)):
		current=x[i]
		j=i-1
		while(j>=0 and x[j]>current):
			x[j+1]=x[j]
			j=j-1
		x[j+1]=current
	return x


print(Insertionsort_asc(inputlist))
