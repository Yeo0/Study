# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:39:51 2018
@author: Yeoyong Na
"""

#####점프투파이썬#####

####02.파이썬 프로그래밍의 기초, 자료형

###02-1. 숫자형

a=1.2
a=4.24E10 #4.24*10^10
a=4.24e-10 #4.24*10^(-10)

a=0o177 #8진수
a=0x8ff #16진수

#사칙연산
a=3
b=4
a*b
a/b
a**b # a^b
a%b #나머지
a//b #나누고 소숫점 버리기 , 즉 가우스 기호
-7//4 #정확히 말하면 왼쪽에 있는 정수 리턴, 즉 가우스 기호


###02-2. 문자형 자료형
# '',"",''',""" 네가지 방법

food = "Python's favorite food is perl" #이 경우 '' 쓸 경우 error
say = '"Python is very easy." he says.' # 이 경우 "" 사용시 error
food = "Python|\'s favorite food is perl" #문자앞에 쓸 경우 문자 그자체로 인식. 사용 가능
multiline = '''
Life is too short
You need python
''' # 여러줄을 한 문자열로 취급 가능
print(multiline)

#문자열 연산
head = "Python"
tail = "is fun!"
head+tail #+로 문자열 이어붙일 수 있음
head*2 #문자열 반복실행

print("="*50)
print("My program")
print("="*50)

#문자열 인덱싱, 슬라이싱
a="Life is too short, You need Python"
a[3] #인덱싱. 0부터 시작. a의 3+1번째 위치한 값이 어떤건지 뽑아냄
a[-3] #뒤에서부터. 뒤에서부터 셀 땐 1부터.

a[0:4] #여러값 뽑아냄. 끝번호 전까지의 값까지. 뽑아내고 싶은 위치+1이 끝번호.
a[0:5] #공백도 하나의 문자로 취급.
a[5:7]
a[:17] #처음부터 17까지
a[19:] #19부터 끝까지
a[:] #문자열 전체를 뽑아냄. 그냥 a쓰면 되는건데 왜 필요할까..?
a[19:-7] #-기호 (뒤에서부터 세는) 사용가능
a[19:-18] #범위가 안맞으면 아무것도 안 반환함

a="20010331Rainy" #문자열 세부분으로 인덱
year=a[:4]
day=a[4:8]
weather=a[8:]
year
day
weather

#문자열 바꾸기
a="Pithon"
a[1]
a[1]='y' #error. 문자열의 요소값은 바꿀 수 있는 값이 아니기 때문
         #문자열, 튜플 등의 자료형은 요소값을 변경할 수 없음

a[:1]
a[2:]
a[:1]+'y'+a[2:] #이런식으로 가능.. 조금 귀찮..

#문자열 포매팅 _ 문자열 내의 특정한 값을 바꿔야할 경우. 문자열 내에 어떤 값을 삽입 _ C에서 주로 쓰이는
#%s=string(어떤거에도 쓸수있는 만능키) / %d= integer
"I eat %d apples" % 3
"I eat %s apples."%"five"

number=3;day="three"
"I eat %d apples" % number
"I ate %d apples. so I was sick for %s days" % (number, day) #,로 변수구분

"I have %s apples" %3
"rate is %s" % 3.234

"Error is %d%." %98 #error. 문자열 포맷코드 %d 와 %가 같은 문자열 내에 존재하는 경우, %를 쓰려면 %%로 써야함.
"Error is %d%%." %98

#포맷코드 +숫자
"%10s" %"hi" #앞에서 10-(hi개수2)칸 띄움 = 전체 길이가 10개인 문자열 공간에서 hi오른쪽 정렬 후 그앞 나머지는 공백으로.
"%-10sjane." % 'hi' #hi 왼쪽정렬 후 나머지는 오른쪽 정렬

"%0.4f" % 3.42134234 # 소숫점 넷째자리까지만
"%10.4f" % 3.421342434 #소숫점 넷째자리까지.왼쪽정렬.

#문자관련 함수들
a="hobby"
a.count('b') #a에서 b개수세기

a="Python is best choice"
a.find('b') #b가 처음나온 위치.
a.find('k') #존재하지 않을땐 -1반환

a="Life is too short"
a.index('t')
a.index('k') #find와의 차이점. 문자열에 존재하지 않으면 에러발생.

a=','
a.join('abcd') #join=문자열 삽입. 각각의 문자 사이에 변수 a값 삽입

a="hi"
a.upper() #소문자 -> 대문자

a="HI"
a.lower() #대문자 -> 소문자

"HI".lower() #변수사요 굳이 안해도

a="   hi    "
a.lstrip() #왼쪽 공백 제거 (한칸 이상의 연속된 공백)
a.rstrip() #오른쪽 공백 제거
a.strip() #양쪽 공백 제거

a="Life is too short"
a.replace("Life","Your leg") #replace(바뀌게 될 문자열, 바꿀 문자열)

a.split()

#고급 문자열 포매팅
"I ate {0} apples".format(3) #{0} 부분이 바뀜. format 함수 이용
"I eat {0} apples".format("five")

number=3
"I eat {0} apples".format(number)

number=10
day="three"
"I ate {0} apples. so I was sick for {1} days.".format(number,day) #{0}.{1}... 인덱스 순서대로

"I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3) #이게 제일 편리한듯하다

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

"{0:<10}".format("hi") # :<10 치환되는 문자열 왼쪽정렬. 총 자리수 10
"{0:>10}".format("hi") # :>10 치환되는 문자열 오른쪽 정렬. 총 자리수 10
"{0:^10}".format("hi") #:^ 가운데 정렬

"{0:=^10}".format("hi") #:■^가운데 정렬, ■문자로 공백 채워줌
"{0:!<10}".format("hi") #왼쪽정렬. 빈공간 !!

y=3.141592
"{0:0.4f}".format(y) #소숫점 넷째자리 까지 포맷팅
"{0:10.4f}".format(y) #소숫점 넷째자리. 자릿수 10.
"{{ and }}".format() #{{}} 연속 괄호로 바로 포맷팅 가능



###02-3. 리스트 자료형
odd=[1,3,5,7,9] #[], 요소들 구분','

a=[] #빈 리스트
b=[1,2,3] #숫자 요소
c=['Life','is','too','short'] #문자 요소
d=[1,2,'Life','is'] #혼합해서 사용가능
e=[1,2,['Life', 'is']] #리스트 자체를 요소값으로 사용 가능

#리스트의 인덱싱
a=[1,2,3]
a
a[0] #리스트 a의 첫번째 요소값
a[0]+a[2]
a[-1] #리스트의 마지막 요소

a=[1,2,3,['a','b','c']]
a[0]
a[-1]
a[3]
a[-1][0] #[a,b,c]에서의 첫번쨰 원소
a[-1][1]
#다중 리스트 인덱싱 역시 동일한 방법

#리스트의 슬라이싱
a=[1,2,3,4,5]
a[0:2] #0부터 2 전까지
a[:2]
a[3:]

a=[1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
a[3][:2]

#리스트 연산자
a=[1,2,3]
b=[4,5,6]
a+b # 리스트 이어 붙이기 (합치기)

a=[1,2,3]
a*3 # * ■ 횟수만큼 반복

a[2]+"hi" #error. 정수와 문자열은 더할 수 없음
str(a[2]) + "hi" #str() : 정수나 실수를 문자열로

#리스트의 수정, 변경과 삭제
a=[1,2,3]
a[2]=4 #a[2]의 요소값만 변경
a

a[1:2] #1부터 2전까지니가 한개만 호출
a[1:2]=['a','b','c'] # a[1]~a[2]사이의 리스트를 바꿈
a[1]=['a','b','c'] #리스트의 두번째 요소를 바꿈. 위와 차이.
a

a[1:3]=[] # a[1],a[2] 삭제
a

del a[1] #del a[i] : i번째 요소값 삭제 / del a[x:y] : x~y번째 요소 사이의 값을 삭제
a

#리스트 관련 함수들
a=[1,2,3]
a.append(4) #append(i) : 마지막에 i추가
a
a.append([5,6]) #리스트 안에는 어떤 자료형도 추가될 수 있음
a

a=[1,2,3,4,3,2]
a.sort() # 정렬함수. 알파벳도 가능 /아예 바꿔버림
a

a=['a','c','b']
a.reverse() # 리스트 역순(현재 리스트를 그대로 거꾸로 뒤집음)
a

a=[1,2,3]
a.index(3) #index(i) = i의 위치값
a.index(1)
a.index(0) #error. 리스트에 없는 값

a=[1,2,3]
a.insert(0,4) # insert(x,y) : x자리에 y삽입
a
a.insert(3,5)

a=[1,2,3,1,2,3]
a.remove(3) # remove(x) : 리스트에서 첫번째로 나오는 x 삭제. 두개 가지고 있을 경우 첫번째 값만 제거
a

a=[1,2,3]
a.pop() # 맨 마지막 요소 return 후 삭제.
a

a=[1,2,3]
a.pop(1) #a[1]의 값 리턴 / 최종적으로 a에선 a[1]값 제거
a

a=[1,2,3,1]
a.count(1) # 1의 개수

a=[1,2,3]
a.extend([4,5]) #a.extend(x):x자리에 리스트만. a+x역할
a

b=[6,7]
a.extend(b) # a+=b와 동일
a
a+=b
a

#리스트 요소를 제거하는 3가지 방법
#1.remove
a=[1,2,3,'a','b','c']
a.remove('a') #remove(x);x는 리스트 내 값 (인덱스 사용불가)
a

#2.pop
a=[1,2,3,'a','b','c']
a.pop(4) #pop(x);x는 인덱스값 (리스트 내 값 사용불가)
a

#del
a=[1,2,3,'a','b','c']
del a[4] #del a[x];x는 인덱스값
a




###02-4. 튜플 자료형
#리스트와의 차이점 : [] vs () / 리스트는 값의 생성,삭제,수정 가능, 튜플은 불가 (한번 정하면 지우거나 변경 불가)

t1=() #빈 튜플
t2=(1,) #차이1. 1개요소 가질땐 뒤에 , 필요
t3=(1,2,3) #괄호 생략해도 무방
t4=1,2,3
t5=('a','b',('ab','cd'))

#-> 프로그램이 실행되는 동안 항상 변하지 않아야 하는 밥이라면 튜플 사용
#리스트 사용횟수가 훨씬 많으나 튜플이 사용되는 경우도 꽤 있음

t1=(1,2,'a','b')
del t1[0] #튜플은 지우는 행위 불가
t1[0]='c' #튜플 요소값 변경 불가

#1. 튜플 인덱싱
t1=(1,2,'a','b')
t1[0]
t1[3]

#2. 튜플 슬라이싱
t1=(1,2,'a','b')
t1[1:]

#3.튜플 더하기
t2=(3,4)
t1+t2

#4. 튜플 곱하기
t2*3 # 반복

#리스트와 사용문법은 동일



###02-5. 딕셔너리 자료형

#대응관계를 나타낼 수 있는 자료형 (Key, value)
#key를 통해 value를 얻음 (자료구조 참고 _ java map과 동일)

dic={'name':'pey','phone':'0119993323','birth':'1118'} #{key:value, key:value, ...}

#1. 딕셔너리 쌍 추가하기
a={1:'hi'}
a={'a':[1,2,3]}

a={1:'a'}
a[2]='b'#key=2,value=b인 딕셔너리 한 쌍 추가
a

a['name']='pey'
a

a[3]=[1,2,3]
a

#2. 딕셔너리 요소 삭제하기
del a[1] #del a[key]: key에 해당하는 {key:value}쌍 제거
a


##딕셔너리 활용
grade={'pey':10, 'julliet':99}
grade['pey']
grade['julliet']

a={1:'a',2:'b'}
a[1] #a[key] -> key 에 해당하는 value 리턴
a[2]

dic={'name':'pey','phone':'0119993323','birth':'1118'} #{key:value, key:value, ...}
dic['name'] #없는 key 일 때 오류
dic['phone']
dic['birth']


##딕셔너리 쓸 때 주의사항
#1. key는 고유한 값이므로 중복될 경우, 누락됨. -> 중복 안쓰는게 좋음
a={1:'a',1:'b'}
a #둘 중 하나는 무시됨

#2.key에 리스트는 쓸 수 없음 (리스트의 변하는 특성 때문)
a={[1,2]:'hi'}

##딕셔너리 관련 함수들
dic={'name':'pey','phone':'0119993323','birth':'1118'} #{key:value, key:value, ...}
dic.keys() #dic의 key만을 튜플로 묶은 값을 dict_keys 객체 리턴

for k in dic.keys():
    print(k)

list(dic.keys()) #dict_keys 리스트변환

dic.values() #dic의 value만을 튜플로 묶은 값을 dict_values 객체 리턴
list(dic.values())

dic.items() #dic의 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체 리턴
list(dic.items())

dic.clear() #key:value 쌍 모두 지우기
dic

dic={'name':'pey','phone':'0119993323','birth':'1118'} #{key:value, key:value, ...}
dic.get('name') #dic['name']과 동일한 기능 / 없는 key일 때 None return
dic.get('phone')

dic.get('nokey')
dic['nokey']

dic.get('foo','bar') #get(x,default값) / foo가 없으므로 디폴트인 bar 리턴

dic={'name':'pey','phone':'0119993323','birth':'1118'} #{key:value, key:value, ...}
'name' in dic #dic에 해당 key있는지 확인 / True or False로 리턴
'email' in dic

#순서가 없기 때문에 인덱싱 불가능


###02-6. 집합 자료형

s1=set([1,2,3])
s1

s2=set("Hello") #중복허용 X, 순서X -> 인덱싱 불가
s2


s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#1.교집합
s1&s2
s1.intersection(s2)

#2. 합집합
s1|s2
s1.union(s2)

#3. 차집합
s1-s2
s2-s1
s1.difference(s2)
s2.difference(s1)

#함수들
s1=set([1,2,3])
s1.add(4) #값 1개 추가
s1

s1.update([4,5,6]) #값 여러개 추가하기
s1

s1.remove(2) #특정 값 제거
s1


###02-7. 불 자료형 (논리 (T/F))
a=True
b=False

1==1
2>1
2<1

a=[1,2,3,4]
while a:
    print(a.pop())
#마지막 요소부터 하나씩 꺼내기

#자료형의 참/거짓 식별
bool('python')
bool('') #빈 문자열 거짓
bool([1,2,3])
bool([]) #빈 리스트 거짓
bool(0) #0거짓
bool(3)



###02-8. 변수

#변수=객체=파이썬에서 사용되는 모든 것

a=1 #a:변수의 이름 = 객체가 저장된 메모리위치 가리키는 레퍼런스
b="python"
c=[1,2,3]
type(3)

import sys
sys.getrefcount(3)
a=3
sys.getrefcount(3)
b=3
sys.getrefcount(3)
#하나씩 늘어남.


#변수를 만드는 여러가지 방법
a,b = ('python','life') #튜플로 변수 생성 가능
(a,b)=('python','life') #위와 동일한 방법
[a,b]=['python','life'] #리스트로 변수 생성 가능

a=b='python'

#변수 바꾸는 함수
a=3
b=5
a,b=b,a #헐ㅋㅋㅋㅋㅋㅋ
b
a

#생성 변수 제거
a=3
b=3
del(a)
del(b)

#리스트를 변수에 넣고 복사하고자 할 때
a=[1,2,3]
b=a
a[1]=4
a
b # 같은 리스트를 가리고 있는 것이기 때문에 같이 바뀜
a is b #간단히 확인 가능

a=[1,2,3]
b=a[:] #리스트 전체를 가리키는 [:]를 이용해 복사
a[1]=4
a
b

from copy import copy
b=copy(a) # = b=a[:]과 동일함

b is a




####03.프로그램의 구조, 제어문

### 03-1. if문

#여러 조건문 있을 때 제일 처음에 해당되는 거만 return 함
#and or not
#"돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라"
money = 2000
card=1

if money>=3000 or card:
    print("택시타")
else:
    print("걸어가")

#in, not in
1 in [1,2,3]
1 not in [1,2,3]

#"만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라"
pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("go by taxi")
else:
    print("go by bus")

#"주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라"
#pass - 아무것도 하고싶지 않게 할떄
pocket=['paper','cellphone','money']
if 'money' in pocket:
    pass
else:
    print("take card out")

if 'money' not in pocket:
    print("take card out") #위에랑 같은 결과

#"주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라"
pocket=['paper','cellphone','money']
card=1
if 'money' in pocket:
    print("taxi")
else:
    if card:
        print("taxi")
    else:
        print("walk")

pocket=['paper','cellphone','money']
card=1
if 'money' in pocket:
    print("taxi")
elif card: #이전 조건이 거짓일 때 수행
    print("taxi")
else:
    print("walk")

#조건부표현식
if score >=60:
    message="success"
else:
    message="faliure"

messeage="success" if score>=60 else "failure"
#조건문 참인경우 if 조건문 else 조건문이 거짓인 경우
#한 라인으로 작성할 수 있어 활용성 좋음

#연습문제1
money=5000
card=False

if card or money >=4000:
    print("you can take taxi")
else:
    print("you can't take taxi")

#연습문제2
a=[1,9,23,46]

if 23 in a:
    print("congratulation")

#연습문제3
def evenornot(a):
    if a % 2 ==0:
        return "even"
    else: return "not even"
evenornot(23)

#연습문제4
a="f,80"
b="m,45"

def morf(a):
    new=a.split(',')
    if 'm' in new:
        if int(new[1]) % 2 ==1:
            print("A")
        else:
            print("B")
    else:
         if int(new[1]) % 2 ==1:
            print("C")
         else:
            print("D")

morf("f,27")

#연습문제5
#skirt



### 03-2. while문

treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    #treeHit+=1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit==10:
        print("나무가 넘어갑니다.")

#ㅕ여러 선택지중 하나를 선택해서 입력받는 예제
prompt="""
    1. Add
    2. Del
    3. List
    4. Quit
    Enter number:"""

number=0
while number !=4:
    print(prompt)
    number=int(input()) #사용자의 숫자입력을 받아들임

#자판기
coffee=10
money=300
while money: #300으로 고정되있음. 0이 아니기에 항상 참을 의미 // while문 내에서 멈춰주거나 조건을 걸고싶을때 항상 참을 사용
    print("돈을 받았습니다")
    coffee=coffee-1
    print("남은 커피양은 %d개 입니다" % coffee)
    if not coffee: #if coffee==0
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break

#실제 자판기
coffee=10
while True:
    moeny=int(input("돈을 넣어주세요:"))
    if money ==300:
        print("커피를 받으세요")
        coffee -=1
    elif money >300:
        print("거스름돌 %d를 돌려주고 커피를 받으세요" %(money-300))
        coffee-=1
    else:
        print("커피를 뽑을 수 없습니다.")
        print("남은 커피양은 %d개 입니다" % coffee)
    if coffee==0:#if not coffee
        print("커피가 다 떨어졌습니다")
        break

#처음으로 돌아가기
a=0
while a<10:
    a+=1
    if a%2==0: continue #while문의 처음으로 가게하는거니 else굳이 쓸 필요x
    else:
        print(a)

a=0
while a<10:
    a+=1
    if a%2==0: continue
    print(a)

a=0
while a<10:
    a+=1
    if not a%2==0:
        print(a)

#무한루프
while True:
    print("something") #빠져나오려면 ctrl+c


#연습문제
#2.1~1000자연수 3배수 합
a=0
b=0
while a<1001:
    if a%3==0:
        b+=a #b=b+a
    a+=1

print(b)

#3.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
a=0
b=0
while a<len(A):
    if A[a]>=50:
        b+=A[a]
    a+=1
print(b)
#답
result=0
while A:
    mark=A.pop()
    if mark>=50:
        result+=mark
print(result)

#5. 왜 오류가나지?
line=0
while line<5:
    print("*"*line)
    line+=1
#답
line=0
while True:
    line+=1
    if line>5: break
    print("*"*line)

#6.
star=7
space=0
while star>0:
    print(""*space+"*"*star)
    star-=2
    space+=1


##03-3.for문
test_list=['one','two','three']
for i in test_list:
    print(i)


a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last) #튜플의 변수값 대입 사용

marks=[90,25,67,45,80]

number=0
for mark in marks: # 리스트 자체가 들어가도됨
    number+=1
    if mark>=60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다" % number)

#continue: 처음으로 돌아가게 함
number=0
for mark in marks:
    number+=1
    if mark<60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

number=0
for mark in marks:
    number+=1
    if mark>60:
        print("%d번 학생 축하합니다. 합격입니다." % number)
    #else: continue

#range
a=range(10) #앞에는 자동으로 0이 들어감 / 시작과 끝 숫자는 포함되지 않음
a

a=range(1,11)
a

sum=0
for i in range(1,11):
    sum=sum+i

print(sum)


#
marks=[90,25,67,45,80]
for number in range(len(marks)): #개수가 들어가도되고 #range(숫자):0~숫자
    if marks[number]<60: continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))

#구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ") #출력값을 줄바꿈없이 이어주기위해
    print("") #문단바꿈


#리스트안에 for 문 포함
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)

print(result)

#짝수에만 3곱해서 담기
result=[num*3 for num in a if num%2==0]
print(result) #리스트 내에서도 가능

#구구단 리스트로
result=[x*y for x in range(2,10)
            for y in range(1,10)] #리스트내에서 함수 두번 사용
print(result)

#언습문제
#2
sum=0
for i in range(1,1001):
    if i % 5 ==0:
        sum+=i

print(sum)

#3
sum=0
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for score in A: #리스트로 쓸때는 그냥 앞에껄로씀
    sum+=score
print(sum/len(A))



#4답
blood=['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result={} #딕셔너리 생성
for i in blood:
    if i in result:
        result[i]+=1 #키값이 존재하는 경우에 기존값에 더함
    else:
        result[i]=1 #없으면 키값 생성

#5
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
result

list=[n*2 for n in numbers if n%2==1]
print(list)

#6
sens="Life is too short, you need python"
aeiou=["a","e","i","o","u"]

''.join([a for a in sens if a not in aeiou])




####04-1 함수
#파라메타: 함수에 입력으로 전달된 값(함수를 만들때)
#아규먼트: 함수를 호출할 때 전달되는 입력값

def sum(a,b): #a,b는 파라메타(매개변수)
    return a+b

print(sum(3,4)) #3,4는 인수(아규먼트)

def say():
    return 'Hi'


say()


#여러개의 입력값을 받을 때 :*
def sumMany(*int):
    sum=0
    for i in int: #ㄹ리스트형식으로 많이사용
        sum+=i
    return sum

sumMany(1,2,3,4)

#
def sumMul(cat,*num):
    if cat=="sum":
        result=0
        for i in num:
            result+=i
    elif cat=="mul":
        result=1
        for i in num:
            result=result*i
    return result

sumMul("sum",1,5,8)
sumMul("mul",1,5,8)

##키워드파라미터 kwargs
##딕셔너리 생성함수 :** 두개
def func(**kwargs):
    print(kwargs) #함수형태
                  # key=value형태의 입력인수가 저장되는 딕셔너리 변수


func(a=1) # a=1의 딕셔너리 생성
func(name='foo',age='3')

#입력인수 형태 다양하면?
def func(*arg, **dic):
    print(arg)
    print(dic)

func(1,2,3,name='foo',age='3')
#앞에 여러개는 인수로, 뒤에는 딕셔너리로 저장됨

#return: 함수를 빠져나가는 방법

def say_nick(nick):
    if nick=="바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick("멍총이")
say_nick("바보") #ㅎ함수 종료

## 매개변수에 초깃값 미리 설정하기(초기화 하고싶은 매개변수는 맨뒤에 위치해야한다!!!)
def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박응용",29) #변수 2개인 것처럼 사용가능
say_myself("박응용",27,True)
say_myself("박응용",27,False)

#함수 안에서 선언된 변수의 효력범위
#함수 안에서 선언된 매개변수는 함수 안에서만 사용된다.
#return이용

a=1
def vartest(a):
    a=a+1
    return a

a=vartest(a)
print(a)


#global이용
a=1
def vartest():
    global a #함수는 독립적이용이 좋기때문에 되도록 안쓰는게 좋음
    a=a+1

vartest()
print(a)

#lambda : 함수를 간결하게 만들때
sum=lambda a,b : a+b
sum(3,4)

def sum(a,b):
    return a+b #와 동일한 기능

#lambda사용하면 def안쓰이는 데에서 함수 사용가능
myList=[lambda a,b:a+b, lambda a,b:a*b]
myList[0](3,4)
myList[1](3,4) 
#어떻게 한번에 받아올까?
newList=[myList[0](3,4),myList[1](3,4)]
newList
myList[0][1](3,4)

#연습문제
#1 홀짝판별
def is_odd(num):
    if num%2==0:
        return False
    else:
        return True
is_odd(3)
is_odd(8)

#2 평균값 계산
def calMean(*num):
    result=0
    for i in num:
        result+=i
    return result/len(num)
        
calMean(3,4,9)

#3 구구단 출력
def gugudan(n):    
    print("****%d단****" % n)
    for i in range(1,10):
        print("{0} * ".format(n),i," =", n*i)
       
gugudan(3)
    
#4 피보나치
def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)
fibo(1)
fibo(6)

for i in range(10):
    print(fibo(i))
    
 #5 5보다 큰수만
def myfunc(nums):
    result=[]
    for num in nums:
        if num>5:
            result.append(num)
    return result
    
myfunc([2,3,5,6,3,49])

myfunc=lambda nums:[num for num in nums if num>5]
    
    
    
### 04-2. 사용자 입출력 관리    
#사용자입력 : input 
a=input()
a

number=input('숫자를 입력하세요:')
print(number)
    
#print 자세히 알기
#1. ""로 둘러싸인 문자열은 +연산과 동일하다
print("life" "is" "too" "short")
print("life"+"is"+"too short")

#2. 문자열 띄어쓰기는 콤마로 한다.
print("life","is","too short")
    
#3. 한 줄에 결과 값 출력하기
for i in range(10):
    print(i, end=" ")
    
#연습문제
#1. 두 수의 합
input1=input("첫번째 숫자를 입력하세요:")
input2=input("두번째 숫자를 입력하세요:")
total=int(input1)+int(input2)
print("두수의 합은 %s입니다" % total)    
    
#2. 숫자의 총합
a=input()   
aList=list(a.split(","))
result=0
for i in aList:
    result+=int(i)
    
result

#4. 한줄 구구단
gugu=input("구구단을 출력할 숫자를 입력하세요(2~9)")
for i in range(1,10):
    print(int(gugu)*i, end=" ")



### 04-3. 파일 읽고 쓰기


## 파일 생성하기
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/new.txt", 'w') #r:read, w:write, a:add
f.close() 
    
## 파일을 쓰기모드로 열어 출력값 적기

# writedata.py
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/new.txt", 'w') #r:read, w:write, a:add
for i in range(1,11):
    data="%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

## 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법

#readline()
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/new.txt", 'r') #r:read, w:write, a:add
line=f.readline()
print(line) 
f.close()    

while True:
    data=input()
    if not data: break
    print(data)

#readlines()
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/new.txt", 'r') #r:read, w:write, a:add
lines=f.readlines() #각각의 줄을 요소로 갖는 리스트로 리턴
for line in lines:
    print(line)
f.close()
    

#read()
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/new.txt", 'r') #r:read, w:write, a:add
data=f.read() #파일 내용 전체 문자열 리턴
print(data)
f.close()

## 파일에 새로운 내용 추가하기

# adddata.py
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/new.txt", 'a') #r:read, w:write, a:add
for i in range(11,20):
    data="%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
    
##with문과 함께 사용하기
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/foo.txt", 'w') #r:read, w:write, a:add
f.write("Life is too short, you need python")
f.close()

with open("/Users/yeoyoung/documents/GitHub/Study/jump2python/new.txt", 'w') as f: 
    f.write("Life is too short, you need python")
#with 사용하면 f 자동으로 close

#sys모듈로 입력 인수 주기
#sys1.py
    
import sys

args=sys.argv[1:]
for i in args:
    print(i)
   
#sys2.py
import sys
args=sys.argv[1:]
for i in args:
    print(i.upper(), end='')
    
    
    
#연습문제
#1.
f1=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/test.txt", 'r')
print(f2.read())

#2.
data=input("저장할 내용을 입력하세요:")
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/test.txt", 'a')
f.write(data)
f.close()

##3.
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/abc.txt", 'r')
data=f.readlines()
f.close()

f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/abc.txt", 'w')
newdata=reversed(data)
for new in newdata:
    new =new.strip()
    f.write(new)
    f.write('\n')
#newdata=newdata.replace("\n","")
#
#f.write(newdata)

f.close()


#4.
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/test.txt", 'r')
data=f.read()
f.close()
data=data.replace("java","python")

f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/test.txt", 'w')
f.write(data)
f.close()

#5.
f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/sample.txt", 'r')
data=f.readlines()
f.close()
#int(data[1])
total=0
for dat in data:
    result=int(dat)
    total+=result
avg=total/len(data)

f=open("/Users/yeoyoung/documents/GitHub/Study/jump2python/sample.txt", 'w')
f.write(str(avg)) # write에는 문자만 사용가능
f.close() 
    


####05-1. 클래스
#클래스 : 같은 기능을 쓰는 함수를 동시에 이용할 때 서로 독립된 값을 쓰기 위해 
#      : 과자틀 -클래스 / 과자틀로 찍어낸 과자들 - 객체(object)
#클래스에 의해 만들어진 객체들은 객체별로 독립적인 성격을 가짐.

class Calculator:
    def __init__(self): #받아오는 역할
        self.result=0 
        
    def add(self, num):
        self.result+=num
        return self.result
    
    def sub(self, num):
        self.result-=num
        return self.result
    
cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))        
print(cal2.add(7)) 


#클래스 쉬운 예제
class Cookie:
    pass #임시 코드 작성할 때 주로 pass사용

a=Cookie() # a=객체 / a는 cookie의 인스턴스
b=Cookie() #한개의 클래스는 무수히 많은 객체를 만들 수 있음

#인스턴스: 특정 객체가 어떤 클래스의 객체인지 설명할 때
#클래스 만들때는 일단 구조 (결과값이 어떻게 나올것인지를)를 생각하고 만드는 게 좋음

class FourCal():
    pass

a=FourCal()
type(a)

#클래스 내의 함수는 메소드(Method)
class FourCal():
    def setdata(self, first, second): #클래스 내의 함수에서 받아올 인수들을 지정할 때 self이용
        self.first=first #a.first의 의미
        self.second=second #a.second의 의미


a.setdata(4,2) #setdata함수의 self = a, first =4, second = 2
 
print(a.first)
print(a.second)

#새로운 메소드 추가
class FourCal():
    def setdata(self, first, second): #클래스 내의 함수에서 받아올 인수들을 지정할 때 self이용
        self.first=first #a.first의 의미
        self.second=second #a.second의 의미
    
    def sum(self):
        result=self.first+self.second
        return result
    
    def mul(self):
        result=self.first*self.second
        return result
    
    def sub(self):
        result=self.first-self.second
        return result
    
    def div(self):
        result=int(self.first / self.second)
        return result
        
a=FourCal()
b=FourCal()

a.setdata(4,2)     
b.setdata(3,7)
        
a.sum()
a.mul()        
a.div()        
b.sum()   
b.sub()     
b.div()        
        
        
##생성자(Constructor) : __init__ : 객체가 생성될 떼 자동으로 호출되는 메소드
class FourCal():
    def __init__(self, first, second): #self:생성되는 객체, first:4, second:2
        self.first=first
        self.second=second
         
    def sum(self):
        result=self.first+self.second
        return result
    
    def mul(self):
        result=self.first*self.second
        return result
    
    def sub(self):
        result=self.first-self.second
        return result
    
    def div(self):
        result=int(self.first / self.second)
        return result
     

a=FourCal(4,2) #처음부터 값을 전달해줘야함
a.sum()
a.div()        

## 클래스의 상속 : 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받게 끔 하는 것
#             : 기존클래스는 그대로 두고 클래스 기능 확장시킬 때 사용.

class MoreFourCal(FourCal): #인수에 다른 클래스를 받아옴
    pass

a=MoreFourCal(4,2) 
a.sum() #앞에 만들어 놓은 함수의 기능을 똑같이 사용 가능


#제곱승
class MoreFourCal(FourCal): #인수에 다른 클래스를 받아옴
    def pow(self):
        result=self.first**self.second
        return result   
    
a.pow()

##Method Overwriting -> 같은 함수를 다시 만들면 이렇게 오버라이팅 된 메소드가 호출됨

class SafeFourCal(FourCal):
    def div(self):
        if self.second==0:
            print("Can't Calculate")
        else:
            return self.first/self.second
    
    
a=SafeFourCal(4,0)
a.div()


##클래스 변수 : 클래스 내에서 선언된 변수
class Family:
    lastname="김"

print(Family.lastname) #함수사용하듯 사용할 수 있음
a=Family()
b=Family()
print(a.lastname)
print(b.lastname)

Family.lastname="박"
print(a.lastname)
print(a.lastname) #클래스 변수는 생성된 모든 객체에 공유됨

id(Family.lastname) #객체 주소 리턴
id(a.lastname)
id(b.lastname)



##클래스의 활용
#나이출력
def print_age(data):
    tmp=data.split("|")
    age=tmp[1]
    print(age)
    
data="홍길동|42|A"
print_age(data)

def print_grade(data):
    tmp=data.split("|")
    name=tmp[0]
    grade=tmp[2]
    print("%s 당신의 점수는 %s입니다." % (name, grade))

data="홍길동|42|A"
print_grade(data)

class Data:
    def __init__(self, data):
        tmp=data.split("|")
        self.name=tmp[0]
        self.age=tmp[1]
        self.grade=tmp[2]


data=Data("홍길동|42|A")
print(data.age)
print(data.name)
print(data.grade)



class Data:
    def __init__(self, data):
        tmp=data.split("|")
        self.name=tmp[0]
        self.age=tmp[1]
        self.grade=tmp[2]
    
    def print_age(self):
        print(self.age)
    def print_grade(self):
        print("%s님 당신의 점수느 %s입니다." % (self.name, self.grade))
        

data=Data("홍길동|42|A")
data.print_age()
data.print_grade()

####연습문제
#1. 
class Calculator:
    def __init__(self):
        self.value=0
        
    def add(self,val):
        self.value+=val
        
cal=Calculator()
cal.add(3)
cal.add(4)

print(cal.value)

#2.
class Calculator:
    def __init__(self, init_value):
        self.value=init_value
        
        
    def add(self, val):
        self.value+=val

       
cal=Calculator(0)
cal.add(3)
cal.add(4)

print(cal.value)


#3.
class Calculator:
    def __init__(self):
        self.value=0
        
    def add(self,val):
        self.value+=val
        
class UpgradeCalculator(Calculator):
    def minus (self, val):
        self.value-=val

cal=UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)    
    
#4.MaxLimitCalculator

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value+=val
        
        if self.value >= 100:
            self.value=100
        

cal=MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)


#5.
class Calculator():
    def __init__(self, list):
        self.list = list
    
    def sum(self):
        return sum(self.list)    
    def avg(self):
        return sum(self.list)/len(self.list)
        
cal1=Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
cal2=Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

#풀이
class Calculator():
    def __init__(self, list):
        self.list=list
        
    def sum(self):
        result=0
        for num in self.list:
            result+=num
        return result
    
    def avg(self):
        total=self.sum()
        return total/len(self.list)

cal1=Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
cal2=Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())



##### 05-2. 모듈
#모듈 : 함수나 변수. 클래스 들을 모아 농흔 파일
#    : 다른 파이썬 프로그램에서 불러와 사용할 수 있게 끔 만들어진 파이썬 파일
# import!!!

import mod1 #현재 디렉토리에 있는 파일이나 파이썬 랑비브러리가 저장된 디렉터리에 있는 모듈만 ㅁ불러올 수 있다.

print(mod1.sum(3,4))


#모듈 함수를 사용하는 또 다른방법
#from 모듈이름 import 함수

from mod1 import * (모든 함수다)


#모듈에 포함된 변수, 클래스, 함수 사용하기
print(mod2.PI)
a=mod2.Math()
print(a.solv(2))

#새 파일 안에서 이전에 만든 모듈 불러오기

#모듈을 불러오는 또 다른 방법
#1.sys.path.append(모듈을 지정한 디렉토리)사용
import sys
sys.path # 파이썬 라이브러리들이 설치되어있는 디렉토리 보여줌
sys.path.append("/Users/yeoyoung/Desktop/python")
sys.path # 이후 모듈 바로 import 가능

#2. pythonpath 환경변수 사용하기



#### 05-3. 패키지
#패키지 : 도트(.)를 이용하여 파이썬 모듈을 계층적(디렉터리 구조) / 디렉터리와 파이썬 모듈로 구성
#모델명이 A.B라면 A:패키지명 , B:모듈

##패키지안의 함수 실행
#set PYTHONPATH=/Users/yeoyoung/Desktop/python

#모듈이 포함되게 임포트 해야함
#1.
import game.sound.echo #제일 마지막은 패키지만 올 수 있음
game.sound.echo.echo_test

#2. #내가 제일 일반적으로 사용하는 방법
from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()


##__init__.py용도
# 있어야 패키지로 인식 (python 2.x버전)



##__all__의 용도
#__init__.py파일에 __all__이라는 변수를 설정하고 import 할 수 있는 모듈을 정의해 주어야함
#from a.b.c import * 에서 c가 모듈이면 상관없지만 그렇지 않은경우 이 과정이 필요함



##relative 패키지
#relative 접근자

# .. : 부모 디렉토리
#. : 현재 디렉토리 

#모듈 안에서만 사용 가능



#### 05-4. 예외처리
#try, except : try블록 실행중에 오류가 발생하면 except블록이 수행/try블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않음
#1. 그냥 try, except만 쓰면 오류가 발생하기만 하면 except 블록 수행
try:

except:

#2. 발생오류만 포함 _미리 정해놓은 오류 이름과 일치할 때만 except블록 수행
try:
    
except 발생 오류:

#3. 발생 오류와 오류 메시지 변수까지 포함_ 오류 메시지 내용까지 알고싶을 때
try:

except 발생 오류 as 오류 메시지 변수


# try문은 else절을 지원. else절은 예외가 발생하지 않은 경우 실행. 반드시 except절 바로 뒤에 위치
try:
    f=open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data=f.read()
    f.close()
#에러가 발생하지 않으면 이어서 실행되는 것

#try.. finally 
#finally- try문 수행 도중 예외 발생 여부에 상관없이 항상 수행됨
#리소스를 close해야 할 경우 많이 사용
    
f=open('foo.txt','w')
try:
    #무언가 수행
finally:
    f.close()

#여러개의 오류처리하기
try:
except 발생오류1:
except 발생오류2:
    
#
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
    
except IndexError as e:
    print(e)
#
try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

##오류 회피하기-pass
try:
    f=open('없는파일','r')
except FillNotFoundError:
    pass

##오류 일부러 발생시키기
#raise

class Bird:
    def fly(self):
        raise NotImplementedError
#Bird클래스를 상속받는 자식 클래스는 반드시 fly함수를 구현해야 한다. 
#만약 자식클래스가 fly함수를 구현하지 않은 상태로 fly함수를 호출하면 어떻게 될까
        
class Eagle(Bird):
    pass

eagle=Eagle()
eagle.fly()

class Eagle(Bird):
    def fly(self):
        print("very fast")    

eagle=Eagle()
eagle.fly()
#새로 구현해야 오류 생기지 않음
    
## 예외만들기 _특수 경우에만 예외처리를 하기위해 종종 예외를 만들어 사용함
#python내장 클래스인 Exception을 상속하여 만듦
class MyError(Exception): 
    pass

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

try:    
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")    
    
 
try:    
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
#위의 경우에 오류메시지가 출력되지 않음. 출력하고 싶다면 __str__메소드 구현해야함.

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"

#따라서 종합해보면 (에러 발생시점에 오류메시지를 출력하고 싶으면)
class MyError(Exception):
    def __init__(self, msg):
        self.msg=msg
        
    def __str__(self):
        return self.msg
    
    
def say_nick(nick):
    if nick=="바보":
        raise MyError("허용되지 않는 별명입니다.")
    print(nick)
    
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
    
##연습문제
#1.
"a"+str(1)   
    
    
a=[1,2,3]
a[-3] #뒤에서 세번째 요소값
    
    
#### 05-5. 내장함수
#abs:절댓값
abs(3)
abs(-3)
    
#all:모두 참이면 True, 거짓이 하나라도 있으면 False
all([1,2,3])    
all([1,2,3,0])    

#any: 하나라도 참이 있으면 True, 모두 거짓이면 False 
any([1,2,3,0])
any([0,""]) 

#chr : 아스키 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력
chr(97)    
chr(48)    

#dir:객체가 자체적으로 가지고있는 변수나 함수를 보여줌.
dir([1,2,3])    
dir({'1':'a'})

#divmod(a,b): a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴
divmod(7,3)
divmod(1.3,0.2)   

#enumerate:순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate객체 리턴
#for문과 함께 자주 사용됨    

for i, name in enumerate(['body','foo','bar']):
    print(i,name)
#자료형의 현제 순서=index와 거기에 해당하는 값을 알 수 있음
#객체가 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 유용
    
#eval :실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수
#보통 입력ㅂ받은 문자열로 파이썬의 함수느 클래스를 동적으로 실행하고 싶은 경우에 사용
eval("1+2")    
eval("'hi'+'a'")
eval('divmod(4,3)') 

#filter(함수이름, 그 함수에 차례로 들어갈 반복 가능한 자료형) - 두번째 인수의 요소들이 첫번째 인수인 함수에 입력됐을때 리턴값이 참인 것만 묶어서 돌려줌.
def positive(l):
    result=[]
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

#=
def positive(x):
    return x>0

print(list(filter(positive,[1,-3,2,0,-5,6])))    
print(list(map(positive,[1,-3,2,0,-5,6] )))
    
list(filter(lambda x:x>0, [1,-3,2,0,-5,6]))  

#hex : 16진수 변환/리턴  
hex(234)
hex(3)    
    
#id : 객체를 입력받아 객체의 고유 주소값(레퍼런스)를 리턴하는 함수
a=3
id(3)  
id(a)    
b=a
id(b) # 3,a,b가 같은 객체 가리키고 있음
id(4)

#input : 사용자 입력 받는 함수 
a=input()    
a    
b = input("Enter :")    
b


#int : 문자열 형태의 숫자 / 소숫점 숫자를 정수 형태로 리턴
int('3')
int(3.4)
int('11',2) #이진수
hex(26)
int('1A',16) #16진수


#isinstance :isinstance(object, class) : 인스턴스,클래스 
#입력받은 인스턴스가 그 클래스의 인스턴스인지 판단하고 참이면 True, 거짓이면 False를 리턴

class Person: pass

a = Person()
isinstance(a, Person) #a가 Person 클래스에 ㅡ이해서 생성된 인스턴스임을 확인

b = 3
isinstance(b, Person)


#len : len(s) 는 s의 길이(요소의 전체 개수)를 리턴하는 함수
len("python")
len([1,2,3])
len((1,'a'))


#list : list(s)는 반복가능한 자료형 s를 입력받아 리스트로 만들어 리턴
list("python")
list((1,2,3))

a = [1,2,3]
b = list(a)
b

#map :map(f,iterable): 함수 f와 반복가능한 자료형을 입력으로 받음
#입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times(x):
    return x*2

list(map(two_times, [1,2,3,4]))

#max : max(iterable) - 최대값을 리턴하는 함수
max([1,2,3])
max("python")

#min : min(iterable) - 최솟값을 리턴
min([1,2,3])
min("python")

#oct(x) : 정수 형태를 8진수 문자열로 바꾸어 리턴
oct(34)
oct(12345)

#open(filename, 읽기방법) - 파일 객체를 리턴. 기본값이 읽기전용모드로 리턴
#w: 쓰기모드 / r: 읽기모
   
f = open("binarly_file","rb")
fred = open("read_mode.txt", 'r')
fred2 = open("read_mode.txt")
fappend = open("append_mode.txt",'a')

#ord : 문자의 아스키 코드 반환
ord('a')
ord('0') 

#pow(a,b) = a**b와 동일
pow(2,4)
pow(3,3)

#range(start,stop,step) - 범위의 값 생성
list(range(5))
list(range(5,10))

list(range(1,10,2))
list(range(0,-10,-1))

#round(number, 자리수) - 반올림
round(4.6)
round(4.2)
round(5.6784, 3)

#sorted(iterable) - 정렬한 후 그 결과를 리스트로 리턴 (원래 리스트를 바꾸진 않음
sorted([3,1,2])
sorted(['a','c','b'])
sorted("zero")
sorted((3,2,1))

#str(object) - 문자열 형태로 객체를 변환
str(3)
str('hi')
str('hi'.upper())

#sum(iterable) - 리스트나 튜플의 모든 요소의 합을 ㅌ리
sum([1,2,3])
sum((4,5,6))

#tuple(iterable) - 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 리턴
tuple('abc')
tuple([1,2,3])
tuple((1,2,3))


#type(object) - 입력값의 자료형이 뭔지 알려줌
type("abc")
type([])
type(open("test",'w'))

#zip(iterable 여러개도 가능)- 동일한 개수로 이루어진 자료형 가능
list(zip([1,2,3],[4,5,6]))
list(zip([1,3,5],[3,5,7],[9,11,13]))
list(zip("abc","def"))


#문제1_내장함수







