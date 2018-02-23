# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:39:51 2018

@author: Yeoyong Na
"""

###점프투파이썬###

##02.파이썬 프로그래밍의 기초, 자료형

#02-1. 숫자형

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


#02-2. 문자형 자료형
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

















