# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # 파이썬, 아나콘다, Jupyter Notebook 시작

# 어 반갑다. 잘 해 보자 ㅋ
# (1장은 내용 없어서 그냥 넘어갔다 ㅋ)

# # 변수와 입, 출력함수

# ## 데이터형과 변수

print("안녕하세요!")

num = 3

num

3 + 5

3 / 5 #알아서 실수 형태의 결과를 출력하네 ㅋ

5 // 3 #몫을 출력

# 문자열 활용

'hello'

a = 'hello'
print(a)

num = 3
type(num)

num2 = 3.0
type(num2)

a = 3
isinstance(a, int)

a = 3
isinstance(a, float)

exist = True #논리형 변수 boolean을 함 만들어 봤다 ㅋ
exist

exist = Frue
exist

# + active=""
# 오타를 내니까 형에 대한 NameError가 나왔지 ㅋ? Boolean은 스펠링 조심하라고 ㅋ
# (참고로 true라고 소문자로 시작해도 에러 난다. 까다로워 죽겠네.)
# -

# ## 변수의 연산

# ### 관계 연산자

a<b #a와 b를 할당하지도 않고 (값을 넣지도 않고)이래 버리니까 에러 나지 ㅋ?

a = 3
b = 5
a > b

a <= b

a == b

a != b

# + active=""
# Quiz 2.9 - p16

# + active=""
# 문제 1번 (내용은 안 베껴 쓸래 궈찮아 죽겠네 ㅋ)
# -

a == 7

# + active=""
# 문제 2번
# -

3 <= b #아이고. 선생님이 이러지 말래. 항상 변수를 왼쪽에 쓰는 걸 권장하시네.

# + active=""
# 문제 3번 ㅋ
# -

a = 3

a >= 3

a != 5

# ## 입.출력 함수

a = 3
b = 5
print(a+b)

# + active=""
# Quiz 2.11 - 자신의 이름을 출력하는 명령문을 작성하시오 ㅋ
# -

print('정지수') # 작은따옴표나 큰따옴표 안의 내용은 전부 string(문자열)로 잘 인식된다 ㅋ

# + active=""
# Quiz 2.12 - 원의 넓이 출력하기 ㅋ
# -

pi = 3.14
r = 2
print(pi*r*r)

import math
r = 2
print(math.pi*r**2) #지수 표기는 이렇게 하면 된다 ㅋ

# + active=""
# p 23 - 내 나이 출력하기
# -

age = 24
print('내 나이는 ', age, '살입니다.') #  +를 쓰는 자바 print()문법... ,를 쓰는 파이썬 print()문법... 헷갈린다 헷갈려!

# + active=""
# Quiz 2.15 - 몫과 나머지
# -

a = 5
b = 3
print('5 // 3 =', a//b) #a 나누기 b의 몫

print('5 % 3 =', a % b) #a 나누기 b의 나머지

# ### 다수의 데이터형 출력

# + active=""
# 아 씨발 데이터형! (입술꽉) .. 어 2, 8, 16, 10진수를 어케 출력하는지 함 봐 보자 ㅋ
# -

two = 0b11 #0b는 2진수의 약자다. (일단 0 써 주고, binary의 약자 b)
print(two)

eight = 0o11 #0o는 8진수의 약자다. (일단 0 써 주고, octal의 약자 o)
print(eight)

seventeen = 0x11 #0x는 16진수의 약자다. (일단 0 써 주고, hexadecimal의 약자 x) (아씨발 16진법이형 왜 약자가 x야!)
print(seventeen)

# ### The Power of Asking for Help

help(print)

# !pip

# ### 입력 함수 input()

# + active=""
# 표준 입력 받기: 문법 ㅋ
# -

print("Enter your name: ")
x = input()
print("Hello, " + x)

type(x) #input()의 타입은 뭘까? 궁금하다.

print(type(x)) #input()으로 들어온 놈은 무조건 str 클래스구나. 알았다.

# + active=""
# 퀴즈) 1 + x의 결과를 나타내시오. (단, x는 input()으로 받은 놈이어야 한다 ㅋ)
# -

x = input()
1 + x #어 정말 int랑 str를 더하려고 하니 않 되지 ㅋ?

1 + int(x) #형변환을 하니 잘 되지?

x = input("1 + x를 계산할 x를 입력해 봐 ㅋ:") #여기서 입력한 input x는 str이다.
print("1 + x = ", 1 + int(x)) #그래서 덧셈하려고 int()로 바꿨다.

# + active=""
# float() 함수로 문자열 입력받은 키(샤이니 키 아님)를 실수형으로 잠만 바꿔 보자.
# -

height = input('키 : ')
print(float(height) + 1.5, 'cm')

# + active=""
# Quiz 2.17 - p 27
# -

print(int('10') + 21)

# + active=""
# Quiz 2.18 - p 28
# -

a = input('변수 a: ')
b = input('변수 b: ')
print(a + b) #string끼리 이어진 것뿐이다.

a = input('변수 a: ')
b = input('변수 b: ')
print(int(a) + int(b)) #형 변환(언니 변환은 없나?)

a = input('변수 a: ')
b = 5
print(a * b) #'3'을 5번 쓴 것처럼 나왔네 ㅋ 애기야 ㅋ

a = input('변수 a: ')
b = 5
print(int(a) * b)

# + active=""
# 29페이지 예제 함 보자.
# -

age = input("나이: ")
print('느그의 10년 뒤 나이는 ' , int(age)+10)
old = age + 10 #어. 윗 라인에서 형변환을 잠깐 한 것뿐이지, 변수 age 자체는 아직 str다. 아예 형을 바꾸려면 age = int(age) 해야 함.
print('그러나? old 변수는 아직 ' , old , '이다 ㅋ') #아쉽게도 문자열 age와 숫자 10을 더할 수 없어서 출력이 안 됨 ㅋ!

# + active=""
# 부울형 데이터값 입력 - Quiz 2.23

# +
adult = input('당신은 성인입니까? [예(1)/아니오(0)]\n') #  \n을 쓰면 사용자는 다음 줄에 입력 가능 ㅋ

adult = int(adult) # input()이기 때문에 str로 들어온 adult를 int로 변환
print(bool(adult)) #얘를 또 부울형으로 출력해 봄 ㅋ
# -
# # 조건문과 반복문

# ## 조건문

# ### if-else문

grade = 80
if (grade > 80):
    print('합격입니다.\n') #파이썬은 중괄호 대신 들여쓰기를 조심해야 한다.
else:
    print('불합격\n')

# + active=""
# 퀴즈) 입력으로 grade를 받은 후 그 값이 80 이상이면 합격, 이하면 불합격!
# -

grade = input('점수를 입력해 주세요: ')
if (int(grade) > 80): #input로 들어온 건 str인 걸 명심해 ㅋ
    print('합격입니다.\n')
else:
    print('불합격\n')

# + active=""
# 퀴즈 2) 표준 입력(input)으로 grade를 받은 후, 그 값이 70 이상이면 C학점, 80 이상이면 B학점, 90 이상이면 A학점

# +
grade = input('점수를 입력해 주세요: ')

if (int(grade) >= 90):
    print('A학점입니다.\n')
elif (int(grade) >= 80): #else if는 파이썬에서 "아예" 안 되네. elif 꼭 기억해 ㅋ.
    print('B학점입니다.\n')
elif (int(grade) >= 70):
    print('C학점입니다.\n')
else :
    print('불합격입니다. ㅋ\n')
# -

# ## 반복문 - for(), while()

# + active=""
# Automate the Boring Stuff with Python!
# -

for i in range(30): #아 맞다 콜론 자꾸 까먹는데 그러지 말아야지 ㅋ
    print('안녕!')

for _ in range(3): #구문 안에서 변수를 활용하는 게 아니라면, 변수 이름 안 써 줘도 가능.
    print('안녕!')

for _ in range(3): #거 봐 구문 안에서 변수를 써야 될 때도 안 쓰면 이상하게 되잖아.
    print(i)

for i in range(3): #음. 제대로 되네. range()도 0부터 시작한다는 걸 잊지 말디 ㅋ
    print(i)

# + active=""
# 퀴즈) 1번 안녕, 2번 안녕, ... , 10번 안녕 코딩을 작성해 보기 ㅋ
# -

for i in range(10):
    print(i+1 , '\b번 안녕')
#1. i는 0번부터 시작하니까, 1번~10번 안녕을 출력하려면 i+1을 출력해야 한다 ㅋ
#2. 멋있는 formatting을 위해 \b라는 특수 기호를 써 봤다. \n이 new line을 의미하듯, \b는 backspace라는 뜻이다.

# + active=""
# Quiz 3.2 - p.41
# -

for i in range(3, 8, 2):
    print(i)

sum = 0
for i in range(1,11):
    sum += i #sum = sum + i
print('합계:', sum)

# ### for문을 이용한 로켓 발사 카운트다운 예제!!1

# + active=""
# Quiz 3.3 - p.41에 있는 놈이다. 얘를 하세요!
# (10부터 1까지 역순 카운트다운, 1초씩 지연, 끝나면 fire!! 하는 놈.)

# + active=""
# 이 연습문제 하나만 따로 잘라내서 혼자 저장한 다음, File - Download as .py - 해서 다운로드 폴더에서 직접 실행해 봤다. 와 재미있다~~~

# +
import time

for i in range(10, 0, -1): #10부터 0보다 1 큰 값까지(1까지) 1씩 감소하는 놈. 1씩 [감소]하니까 꼭 -1이라고 쓰는 거 잊지 마.
    print(i)
    time.sleep(1) #time.sleep(1) 안 쓰면 컴퓨터가 야비한 딩초 술래잡기하듯 십구팔칠육오사삼이일땡!!! 이러고 바로 출력해 버린다. 인내심 없는 놈.
print('Fire!!!!')
# -
# ### 중첩 for문

# + active=""
# 중첩 for문을 만들 때는 indentation에 특히 조심하도록 해 ㅋ 왼지 알갣지 ㅋ 애기야 ㅋ
# -

for i in range(3):
    print('/') #이 놈을 넣으니까 i가 조종하는 범위랑 j가 조종하는 범위랑 확실히 구분이 가지 ㅋ?
    for j in range(3):
        print("* ")

# + active=""
# 교수님께서 다중 for문을 설명하면서 지구와 달, 해 예시를 드셨다.
# 달이 열라게 뺑뺑 돌 때 지구가 한 번 돌고... 그 지구도 사실은 열라게 뺑뺑 태양 주위를 돌고 하는 굉장히 시적인 예시를 드셨다.
# 아 말로 써 놓으니까 굉장히 쌈마이한데 삽화가 굉장히 코페르니쿠스가 좋아할 느낌이었다고..
# -

for i in range(3):
    for j in range(3):
        print("* ", end = '') #파이썬의 print() 문법을 잘 봐라. end 이런 것도 할 수 있다 ㅋ
        # print("* ", end = '\bend') 해 보면 무슨 얘긴지 알 거다. 구부린다는 얘기 아니야... \b랑 end를 붙여 쓴 거야...

# + active=""
# w3schools의 print() 함수 설명을 보자. https://www.w3schools.com/python/ref_func_print.asp
# end는 optional한 건데, 각각의 print한 내용 뒤에 뭘 넣을지 얘기하는 놈이다. 디폴트값은 \n이다. (line break)
# \n이 아니라 스페이스를 넣으라 하니까 쟤의 출력값이 저렇게 되는 거지 ㅋ
# -

for i in range(3):
    for j in range(3):
        print("* ", end = '') #이건 j가 '유키스를 조종하는 흑마술사'처럼 조종하는 놈
    print(' ') #이건 i가 조종하는 놈인데, end를 명시하지 않았기 때문에 \n을 한다.

# + active=""
# 구구단 예시를 함 만들어 보자 ㅋ
# -

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end = '\t') #end를 디폴트값 \n으로 하지 말고 간격 넣을 용도로 \t (탭)해 보자 ㅋ
    print()

# ### 구구단을 ~아주 멋지게~ 출력해 보자 ㅋ

# + active=""
# 교과서 Quiz 3.4 (p 44) 내용이다.
# 어? 나 아직 시작도 안 했는데 쉬는 시간 끝났다고 답 보여 주시는??
# 에이 그냥 답 쓰자 모르겠다...
# -

for i in range(1, 10):
    print('[', i, '단', ']')
    
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)
    print('\n') #이걸 print('\n')이라고 안 하고 print(\n)이라고 하면 또 Syntax Error 뜸 ㅋ

# + active=""
# 교과서 Quiz 3.5도 한 번 해 보자 ㅋ
# -

for i in range(1,4):
    for j in range(1, i+1):
        print(j, end = ' ')
    print() #이렇게만 써도 end를 명시하지 않았으니 알아서 \n을 찍는 거지.

# ### while문

i = 0
while(i<3):
    print(i)
    i = i+1  #i += 1이라고 해도 된다. 희한하게 i++은 파이썬 문법에서는 안 되네. 

# + active=""
# 얘는 이 for문이랑 같다.
# -

for i in range(3):
    print(i)

# # 헐. 이러다 문서 터지겠다 4장은 꼭 Notebook 분리해서 만들자~~~ 하하하~~~
