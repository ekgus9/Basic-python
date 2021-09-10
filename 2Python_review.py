# 1. 파이썬이란?
    # 인터프리터 방식 (<-> 컴파일 방식)

# 2. 자료형, 리터럴과 변수

    # 변수 (int, float, complex, bool, str, list)
        # 파이썬은 모든 자료가 객체
        # 변수는 다른 객체를 참조하는 역할 = 주소를 알고 있음

        # 변수 값이 바꾸면 쓸모없어진 이전 객체 소멸

number = None

# 3. 파이썬의 연산

5/4 # 실수의 나눗셈
5//4 # 정수 연산
2**5 # 제곱
# x+=1
# >, <, >=, <=, ==, !=
# or, and, not

    # is : 같은 객체 참조하는지 비교
        # == : 참조 객체의 내용 같은지 비교

'a' in 'banana'

# 4. 함수 호출과 입출력 함수
    
    # 함수 호출
        # y = sum(a,b)

    # 키보드 입력 함수

age = int( input("나이를 입력하세요."))

    # 화면 출력 함수

print(age)

# 5. 제어 구조와 반복

    # branching : if, else, elif

if age % 2 == 0 : print("짝수")
elif age % 2 != 0 : print("홀수")

    # looping
        # for n in range(2,10,1): # 2-9
        # while n < 10 :
            # print("%2d x %2d = "%(dan, n), dan*n)
            # n += 1

# 6. 컬렉션 자료형

    # 문자열 str
        # m[-1] # 끝

        # "당신의 학점 : %4.1f"% score
        # "취미=%s, 나이=%d"% (hobby, age) # tuple

    # list

big = []
big = [2,3,"ak"]
big.append("mk")

    # tuple
        # 크기나 값 변경 불가

a = (2,)

    # dict

map = {"김연아":"피겨", "류현진":"야구"}
map["김연아"]

    # 집합 set
        # 중복, 순서 없음

b = set()

s1 = {1,2,3}
s2 = {2,3,4,5}
s3 = s1.union(s2) # 합집합
s4 = s1.intersection(s2) # 교집합
s5 = s1 - s2 # 차집합

# 7. 사용자 정의 함수

def Find_max(A):

    max = A[0]

    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]

    return max

    # 디폴트 인수 : 기본값 지정
    # 키워드 인수 : 이름 지정, 순서 상관 없음

# 8. 변수의 범위
    # 내장, 전역(global perimeter), 지역, 인스턴스

# 9. 모듈과 이름 공간
    # import 파일이름 : 사용자 정의 함수 불러올 수 있음

from math import pow , sqrt
from math import * # 모듈에서 모든 식별자 사용 가능

# 연습문제 1. 함수 선언 및 사용

def value_add(v1,v2,num):
    v1 += num
    v2 += num

def List_add(li,num):
    for i in range(0,len(li),1): li[i] += num

val1 = 10
val2 = 20
listA = [10,20,30,40,50]
print(val1,val2,listA)

num = int(input("input int : "))
value_add(val1,val2,num)
List_add(listA,num)
print(val1,val2,listA)

# 연습문제 2. 메뉴를 이용하여 리스트에 친구 이름 관리

mylist = []

while True:
    n = int(input("************\n1. 이름 추가\n2. 이름 삭제\n3. 이름 수정\n4. 종료\n메뉴 선택 : "))
    if n == 1 : 
        name = input("이름 : ")
        if name in mylist: 
            print("이미 있는 이름")
        else :
            mylist.append(name)
            print(mylist)
    elif n == 2 :
        name = input("이름 : ")
        if name not in mylist:
            print("해당 이름 없음")
        else :
            mylist.remove(name)
            print(mylist)
    elif n == 3 :
        name = input("이름 : ")
        if name not in mylist:
            print("해당 이름 없음")
        else :
            newname = input("새이름: ")
            mylist[mylist.index(name)] = newname
            print(mylist)
    elif n == 4 :
        break
    else: print("error")

# 과제 : 번호 맞추기 게임

def compare_answer(right, input):
    if input == right: return 0
    elif input > right: return 1
    elif input < right: return -1

import random

n = random.randint(10,99)
count = 0

for i in range(10):
    count += 1
    n_in = int(input("두자리 정수 입력 : "))
    if compare_answer(n,n_in) == 0: 
        print("정답입니다. %d번 만에 맞추셨습니다\n게임 끝!!!"%count)
        break
    elif compare_answer(n,n_in) == -1: 
        print("아닙니다. 더 큰 숫자입니다!")
    elif compare_answer(n,n_in) == 1: 
        print("아닙니다. 더 작은 숫자입니다!")