
# 1. 자료구조와 알고리즘

    # 자료구조: 컴퓨터에서 자료들을 정리하고 조직화하는 다양한 구조

        # 선형: 항목들을 순서적으로 나열
            # EX) 리스트; 스택, 큐, 덱
        
        # 비선형: 항목들이 보다 복잡한 연결 관계 가짐
            # EX) 트리(힙 트리, 이진 탐색트리), 그래프
    
    # 알고리즘: 특정한 일을 수행하는 명령어들의 집합
        
        # 조건: 입력, 출력; 명백성, 유한성, 유효성
            # + Better algorithm complex data structure
        
        # 기술 방법: 자연어, 흐름도, !유사코드, 특정언어(파이썬)

# 2. 추상 자료형 ADT
    # 자료구조를 프로그램으로 구현할 때 데이터 저장할 구조를 생성하고, 
    # 탐색, 삽입, 삭제 등의 연산을 정형화 시킨 개념

    # EX) Bag 추상 자료형의 구현
        # Bag() : 비어 있는 가방을 새로 만든다.
        # insert(e) : 가방에 항목 e를 넣는다.
        # remove(e) : 가방에 e가 있는 검사하여 있으면 이 항목을 꺼낸다.
        # contains(e) : 항목 e가 들어있으면 True를, 없으면 False를 반환한다.
        # count() : 가방에 들어있는 항목의 합을 반환한다.

def contain(bag, e):
    return e in bag
def insert(bag, e):
    bag.append(e)
def remove(bag, e):
    bag.remove(e)
def count(bag): 
    return len(bag)

mybag = []
insert(mybag, "phone")
insert(mybag, "card")
insert(mybag, "money")
remove(mybag, "phone")
print(contain(mybag, "phone"))
print(count(mybag))

# 3. 알고리즘의 성능분석
    # 알고리즘이 수행하는 연산의 횟수를 측정하여 비교
    # 시간 복잡도 분석

    # 1) 실행시간 측정

import time

mybag = []
start = time.time()
insert(mybag, "ball")
end = time.time()
print(end-start)

    # 2) 복잡도 분석 (시간복잡도 함수: T(n))
        # EX) 삽입 연산

mybag.append("a") # 효율적

mybag.insert(0, "b") # 비효율적 : 가방의 모든 물건을 먼저 이동해야 삽입 가능

    # 빅오 표기법
        # 두 함수 f(n)과 g(n)이 주어졌을 때 모든 n > n0에 대해 f(n) <= c g(n)을 만족하는 상수 c와 n0가 존재하면 f(n) = O(g(n))

sum = 0
n=2

for i in range(1,n+1): # T(n) = 2n^2 + n + 1 -> 차수 큰 항 절대적 -> O(n^2)
    for j in range(1,n+1):
        sum = sum + 1

# 4. 시간 복잡도 분석 : 순환 알고리즘 (재귀호출)

    # 팩토리얼 구하기

def fac(n): # 재귀호출
    if n ==1 :
        return 1
    else :
        return n * fac(n-1)

def fac1(n): # !반복문
    result = 1
    for i in range(1,n+1):
        result = result * (i + 1)

    # 거듭제곱 계산

def power(x, n): # 반복구조 O(n)
    result = 1
    for i in range(n):
        result = result * x
    return result

def power1(x,n): # !순환구조 O(log n)
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return power1(x*x, n//2)
    else :
        return x * power1(x*x, (n-1)//2)

    # 피보나치 수열

def fib(n): # 순환 O(2^n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fib(n-1) + fib(n-2)

def fib1(n): # !반복 O(n)
    last = 0
    current = 1
    if (n<2):
        return n
    else:
        for i in range(2, n+1):
            tmp = current
            current += last
            last = tmp
    return current

    # 하노이 탑 과제
        # A 막대의 원판을 모두 C 막대로 옮기기 (B 임시 막대)
        # 한 번에 원판 하나씩
        # 반드시 큰 판 위 작은 판

def hanoi_tower0(n, fr, tmp, to):
    if (n == 1):
        print("원판 1: %s --> %s" % (fr, to))
    else :
        hanoi_tower0(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower0(n-1, tmp, fr, to)

hanoi_tower0(4,"A", "B", "c")

    # + 총 이동 횟수 추가
    # 한 프로그램에서 n=1, 2, 3, 4 일 때 모두 실행

count = 0

def hanoi_tower(n, fr, tmp, to):

    for i in range(1, n+1):

        def hanoi_in(i, fr, tmp, to):
            if (i == 1):
                print("원판 1: %s --> %s" % (fr, to))
            else :
                hanoi_in(i-1, fr, to, tmp)
                print("원판 %d: %s --> %s" % (i, fr, to))
                hanoi_in(i-1, tmp, fr, to)
        
        hanoi_in(i, fr, tmp, to)
    
        global count
        count = 2**i - 1

        print("총횟수 : ", count)
        print("================")

hanoi_tower(4, "A", "B", "c")