N=int(input("배열 크기를 입력하세요: "))

inputlist=[]

for i in range(N):
	element = input("배열의 원소를 입력해 주세요: ")
	inputlist.append(element)


print(inputlist)

def Mergesort_asc(x,p,q):
	if(p<q):
		k=int((p+q)/2)
		Mergesort_asc(x,p,k)
		Mergesort_asc(x,k+1,q)
	
		return Merge(x,p,k,q)

def Merge(x,p,k,q):
	i=p
	j=k+1 
	l=p #l : 결과 배열의 인덱스
	result=[]

	while(i<=k and j<=q): #각 배열끼리의 비교
		if(x[i]<=x[j]): # 앞배열 첫번째 값이 뒷배열 첫번째 값보다 작으면
			result[l]=x[i] #결과의 첫번재는 앞배열의 첫번째 값이 됨
			i+=1
		else: # 뒷배열 첫번째 값이 더 크면
			result[l]=x[j]
			j+=1
		
		l+=1

	if(i>k): #왼쪽이 다 처리된 경우
		for index in range(j, q+1):
			result[l]=x[index]
			l+=1
	else: #오른쪽이 다 처리된 경우
		for index in range(i,k+1):
			result[l]=x[index]
			l+=1

	for index in range(p,q+1):
		x[index]=result[index]



print(Mergesort(A,0,999))
