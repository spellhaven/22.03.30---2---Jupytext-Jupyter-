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

# ## 오늘은 p.24까지만 하고 끝! 다음에 보자 크킄!








