import random

def Quicksort(A,left,right):

	if left < right:
		#pivot=random.sample(A, 1)
		#p=A.index(pivot)
		p = random.randint(left, right) 
		pivot = A[p]
		
		#피봇을 제일 처음과 바꿈
		temp=A[left]
		A[left]=pivot
		pivot=temp	

	le=left
	ri=right

	for i in range(right-left):

		if A[i] < pivot: #pivot보다 작으면 왼쪽으로 올믹ㅁ
			temp=A[i]
			A[i]=A[le]
			A[le]=temp
			le+=1
	
		#pivot을 자신보다 큰 원소들의 첫번째 원소와 바꿔줍니
		temp=A[le]
		A[le]=A[right]
		A[right]=temp

		p=le
		pivot=A[p]


	l=Quicksort(A,left,p)
	r=Quicksort(A,p+1,right)

	return l+A[p]+r




A=list(range(1,1001))
random.shuffle(A)
print(Quicksort(A,1,1000))
