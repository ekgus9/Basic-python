# 1. 리스트란?
    # 순서를 가진 항목들의 모임
    # 임의의 위치에서도 항목의 삽입, 삭제 가능

    # 리스트의 추상 자료형
        # List() : 임의의 새로운 리스트 만듬
        # insert(pos, e) : 새로운 요소 삽입
        # delete(pos)
        # isEmpty()
        # getEntry(pos)
        # size()
        # clear()
        # find(item)
        # replace(pos, item)
        # sort()
        # merge(lst)
        # display() : 화면에 리스트 출력
        # append(e)

    # 리스트 구현 방법
        # 배열구조 array (파이썬 리스트)
            # 구현 간단, 항목 접근 O(1)
            # 삽입, 삭제시 오버헤드, 항목 개수 제한

        # 연결된 구조 linked list
            # 구현 복잠, 항목 접근 O(n)
            # 삽입, 삭제 효율적, 항목 개수 무한

# 2. 파이썬 리스트

A = [1,2,3,4,5]

len(A) # 항목 수
A.append(6)
A.insert(0,0)

    # 동적 배열

    # 시간 복잡도
        # append(e) : O(1)
        # pop() : O(1)

        # insert(pos,e) : O(n)
        # pop(pos) : O(n)

# 3. 배열로 구현한 리스트
    # 추상자료형 ADT를 함수로 구현

    # 함수 버전

items = [] # 전역변수

def insert(pos,elem): items.insert(pos,elem)
def delete(pos): return items.pop(pos)
def getEntry(pos): return items[pos]
def isEmpty(): return len(items) == 0
def size(): return len(items)
def clear(): 
    global items
    items = []
def find(item): return items.index(item) # 인덱스 반환
def replace(pos, elem): items[pos] = elem
def sort(): items.sort()
def merge(lst): items.extend(lst)
def display(msg = 'ArrayList: '): print(msg, size(), items)

    # 클래스 버전

class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self,pos,elem): self.items.insert(pos,elem)
    def delete(self,pos): return self.items.pop(pos)
    def getEntry(self,pos): return self.items[pos]
    def isEmpty(self): return self.size() == 0
    def size(self): return len(self.items)
    def clear(self): 
        self.items = []
    def find(self,item): return self.items.index(item) # 인덱스 반환
    def replace(self,pos, elem): self.items[pos] = elem
    def sort(self): self.items.sort()
    def merge(self,lst): self.items.extend(lst)
    def display(self,msg = 'ArrayList: '): print(msg, self.size(), self.items)

    def merge_2(self,otherlst): # 두 객체 merge
        self.items.extend(otherlst.items)

# 4. 리스트의 응용 : 라인 편집기
    # 라인 단위로 입력이나 삭제 할 수 있는 문서 편집기

    # 기능
        # i 라인 삽입. 행 번호와 문자열을 입력하면 그 행에 한 라인 추가
        # d 한 라인 삭제. 행 번호 입력하면 그 행을 삭제
        # r 한 라인 변경. 행 번호와 문자열을 입력하면 그 행의 내용 변경
        # p 현재 내용 출력. 현재 문서 모든 내용을 라인 번호와 함께 출력
        # l 파일 입력. 지정된 파일로부터 라인 읽음
        # s 파일 출력. 지정된 파일로 편집 내용 저장
        # q 종료.

def myLineEditor():
    listA = ArrayList()
    while True:
        command = input("i-입력 d-삭제 r-변경 p-출력 l-파일 읽기 s-파일 저장 q-종료")
        
        if command == "q": return
        elif command == "i":
            pos = int(input("입력할 행번호: "))
            str = input("입력할 내용: ")
            listA.insert(pos,str)
        elif command == "d":
            pos = int(input("삭제할 행번호: "))
            listA.delete(pos)
        elif command == "r":
            pos = int(input("수정할 행번호: "))
            str = input("수정할 내용: ")
            listA.replace(pos,str)
        elif command == "p":
            print("Line Editor")
            for i in range(listA.size()):
                print("[{:2d}]".format(i))
                print(listA.getEntry(i))
        elif command == "l":
            inflie = open("test.txt","r")
            lines = inflie.readlines()
            for i in lines:
                listA.insert(listA.size,i.rstrip("\n"))
            inflie.close()
        elif command == "s":
            outfile = open("test.txt","w")
            for i in range(listA.size()):
                outfile.write(listA.getEntry(i)+"\n")
            outfile.close()
            
myLineEditor()

# 과제 : 라인 편집기 클래스 버전으로 구현

class myLineEditor():
    def __init__(self):
        self.listA = ArrayList()

        while True:
            self.command = input("i-입력 d-삭제 r-변경 p-출력 l-파일 읽기 s-파일 저장 q-종료 => ")

            if self.command == "q": return
            elif self.command == "i":
                pos = int(input("입력할 행번호: "))
                str = input("입력할 내용: ")
                self.listA.insert(pos,str)
            elif self.command == "d":
                pos = int(input("삭제할 행번호: "))
                self.listA.delete(pos)
            elif self.command == "r":
                pos = int(input("수정할 행번호: "))
                str = input("수정할 내용: ")
                self.listA.replace(pos,str)
            elif self.command == "p":
                print("Line Editor")
                for i in range(self.listA.size()):
                    print("[{:2d}]".format(i))
                    print(self.listA.getEntry(i))
            elif self.command == "l":
                inflie = open("test.txt","r")
                lines = inflie.readlines()
                for i in lines:
                    self.listA.insert(self.listA.size(),i.rstrip("\n"))
                inflie.close()
            elif self.command == "s":
                outfile = open("test.txt","w")
                for i in range(self.listA.size()):
                    outfile.write(self.listA.getEntry(i)+"\n")
                outfile.close()

myLineEditor()