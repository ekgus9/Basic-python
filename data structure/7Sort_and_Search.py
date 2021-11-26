# 1. 정렬
    # 데이터를 순서대로 재배열 -> 오름차순, 내림차순
    # 정렬된 자료는 탐색에 효율

    # 레코드 : 정렬 대상 -> 여러 필드로 이루어짐
        # 정렬 키 : 정렬 기준 되는 필드
        # 정렬이란 레코드들 키의 순서로 재배열

    # 단순, 비효율 -> 선택, 삽입, 버블 정렬
    # 복잡, 효율 -> 쾩, 힙, 병합, 기수 정렬
    # 정렬 알고리즘의 안정성 : 동일한 키 값 가지는 레코드들이 정렬 후에도 상대 순서 동일 (삽입, 버블, 병합)

# 2. 간단한 정렬 알고리즘

    # 선택 정렬 Selection sort -> O(n^2)
        # 리스트에서 가장 작은 숫자 선택하여 리스트 앞으로 옮기는 방법

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if A[j]<A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A,i+1)

def printStep(arr,val):
    print(" Step%2d="%val,end='')
    print(arr)

data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
selection_sort(data)
print("Selection : ",data)

    # 삽입 정렬 Insertion sort -> O(n^2)
        # 정렬되어 있는 부분에 새로운 레코드를 올바른 위치에 삽입하는 과정 반복, 많은 이동 필요

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A,i)

    # 버블 정렬 Bubble sort -> O(n^2)
        # 인접한 2개 레코드 비교하여 순서대로가 아니면 교환
        # 여러 번 반복

def bubble_sort(A):
    n = len(A)
    for  i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
        if not bChanged: break
        printStep(A,n-i)

# 4. 탐색과 맵구조

    # 탐색 : 테이블에서 원하는 탐색키 가진 레코드 찾는 작업
    # 맵 : 엔트리 또는 키 가진 레코드의 집합
    # 엔트리 : 키, 값으로 이루어짐

# 5. 간단한 탐색 알고리즘

    # 순차 탐색 sequential search
        # 정렬되지 않은 배열을 처음부터 마지막까지 하나씩 검사
        # 평균 (n+1)/2번 비교 (최악 n번 -> 찾는 항목 없음)

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s:%s"%(self.key,self.value))

def sequential_search(A,key,low,high):
    for i in range(low,high+1):
        if A[i].key == key:
            return i
    return None

arr1 = [Entry(9,10),Entry(5,20),Entry(8,30),Entry(3,40),Entry(7,50)]
res = sequential_search(arr1,8,0,4)
for en in arr1:
    print(en,end=' ')
print('\nkey=8 : value={}'.format(arr1[res].value))

    # 이진 탐색 binary search -> O(log n)
        # 정렬된 배열의 탐색 -> 중앙값 조사 후 찾고자 하는 항목 왼쪽인지 오른쪽인지 찾으며 탐색 범위 반으로 줄여 나감

def binary_search(A,key,low,high):
    if low<=high:
        middle = (low+high)//2
        if key == A[middle].key:
            return middle
        elif key<A[middle].key:
            return binary_search(A,key,low,middle-1)
        else:
            return binary_search(A,key,middle+1,high)
    return None

# 6. 고급 탐색 구조 : 해싱
    # 키 값을 적절히 변환하여 인덱스로 사용
    # 키 값 산술적 연산에 의한 테이블 주소 계산

    # 해시함수: 키 값에 의해 데이터 저장된 위치 계산 -> 해시 주소 생성
    # 해시 테이블: 해시함수에 의해 계산된 위치에 데어터 저장된 테이블

    # 충돌 : 서로 다른 키가 해시 함수에 의해 같은 주소로 계산
    # 오버플로: 충돌에 의해 해당 주소에 더 이상 저장 공간 없는 상태

    # 충돌 처리 방법
        # 선형조사
            # 충돌 일어나면 해시터이블 다음 위치에 저장
            # 삭제 연산에서 한번도 안 사용한 버킷과 삭제된 버킷 구분하여야 탐색 오류 안일어남

        # 이차조사
            # 군집화 완화
            # (h(k)+i*i)%M -> h(key),h(key)+1,h(key)+4,h(key)+9 ... (i: 횟수, M: 크기)

        # 이중해싱법(재해싱)
            # 군집화 완화
            # 충돌이 발생하면 다른 해시 함수 이용하여 다음 위치 계산
            # 해시 함수 값이 같아도 키 다르면 다른 위치 가능(함수 두개 쓰니까)
            # h(key)=key%13 , d(key)=7-(key%7) => (h(key)+j*d(key))%13

        # 체이닝
            # 하나의 버킷에 여러 개의 레코드 저장(새로운 노드 이용)

        # 좋은 해시함수: 충돌 적고, 계산 빠름

        # 탐색키가 문자열

def hashFn(key):
    sum = 0
    for c in key:
        sum = sum +ord(c) # 아스키 코드 값
    return sum%M

        # 해싱 적재 밀도 = 저장된 항목 수 / 해싱 테이블 버킷 수
        # 해싱 탐색, 삽입, 삭제: 최선 O(1), 최악 O(n)

# 7. 맵의 응용: 나의 단어장

    # 리스트를 이용한 순차탐색 맵

class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s:%s"%(self.key,self.value))

class SequentialMap:
    def __init__(self):
        self.table = []
    def size(self): return len(self.table)
    def display(self,msg):
        print(msg)
        for e in self.table:
            print(" ",e)
    def insert(self,key,value):
        self.table.append(Entry(key,value))
    def search(self,key):
        pos = sequential_search(self.table,key,0,self.size()-1)
        if pos is not None: return self.table[pos]
        else: return None
    def delete(self,key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return

map = SequentialMap()
map.insert("data","자료")
map.insert("structure","구조")
map.insert("sequential search","선형 탐색")
map.insert("game","게임")
map.insert("binary search","이진 탐색")
map.display("나의 단어장: ")
print("탐색: game --> ", map.search("game"))
print("탐색: over --> ", map.search("over"))
print("탐색: data --> ", map.search("data"))
map.delete("game")
map.display("나의 단어장: ")

# 체이닝 이용한 해시 맵

class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

class HashChainMap:
    def __init__(self,M):
        self.table = [None]*M # 크기 M 고정
        self.M = M
    def hashFn(self,key):
        sum = 0
        for c in key:
            sum=sum+ord(c)
        return sum%self.M
    def display(self,msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d]->"%idx,end="")
                while node is not None:
                    print(node.data,end="->")
                    node = node.link
                print()
    def search(self,key):
        idx = self.hashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node = node.link
        return None
    def insert(self,key,value):
        idx = self.hashFn(key)
        self.table[idx] = Node(Entry(key,value),self.table[idx])
    def delete(self,key):
        idx = self.hashFn(key)
        node = self.table[idx]
        before = None
        while node is not None:
            if node.data.key == key:
                if before == None: self.table[idx] = node.link
                else: before.link = node.link
                return
            before = node
            node = node.link
