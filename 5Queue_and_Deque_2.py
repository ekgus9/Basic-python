# 4. 덱이란?
    # 전단과 후단에서 모두 삽입, 삭제가 가능한 큐

from Queue import *

class CircularDeque(CircularQueue): # 상속
    def __init__(self):
        super.__init__()

    def addRear(self,item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self,item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front-1+MAX_QSIZE)%MAX_QSIZE
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear-1+MAX_QSIZE)%MAX_QSIZE
            return item
    def getRear(self):
        if not self.isEmpty():
            return self.items[self.rear]

# 5. 우선순위 큐
    # 삽입: 배열 뒤 추가
    # 삭제: 저장 항목 중 우선 순위 가장 큰 항목 삭제

class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def clear(self): self.items = []
    def enqueue(self,item): # O(1)
        self.items.append(item)
    def findMaxIndex(self): # O(n)
        if self.isEmpty(): return None
        else :
            highest = 0
            for i in range(1,self.size()):
                if self.items[highest][2]<self.items[i][2]: # 튜플 index 2 비교
                    highest = i
            return highest
    def dequeue(self): # O(n)
        highest = self.findMaxIndex() 
        if highest is not None:
            return self.items.pop(highest)
    def peek(self): # O(n)
        highest = self.findMaxIndex() 
        if highest is not None:
            return self.items[highest]

# 6.  우선 순위 큐의 응용 : 전략적인 미로 탐색
    # 가까운 값 선택

    # 큐에 저장되는 항목 (x,y,-d) 튜플
        # 가까울수록 우선순위 높게 하기 위해 음수로 변환

import math

(ox,oy)=(4,5) # 출구 위치

def dist(x,y):
    (dx,dy) = (ox-x,oy-y)
    return math.sqrt(dx*dx+dy*dy)

def isValidPos(x,y):
    if x<0 or y<0 or x>=MaxSize or y>=MaxSize:
        return False
    else:
        return map[x][y]=='0' or  map[x][y]=='x'

def smartSearch():
    q = PriorityQueue()
    q.enqueue((1,0,-dist(1,0)))
    print("PQueue:")

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2],end='->')
        x,y,_ = here
        if map[x][y] == 'x': return True
        else:
            map[x][y]='.'
            if isValidPos(x-1,y): q.enqueue((x-1,y,-dist(x-1,y)))
            if isValidPos(x+1,y): q.enqueue((x+1,y,-dist(x+1,y)))
            if isValidPos(x,y-1): q.enqueue((x,y-1,-dist(x,y-1)))
            if isValidPos(x,y+1): q.enqueue((x,y+1,-dist(x,y+1)))
            print("우선순위큐 :", q.items)
    return False

map = [['1','1','1','1','1','1'],
        ['0','0','1','0','0','1'],
        ['1','0','0','0','1','1'],
        ['1','0','1','0','1','1'],
        ['1','0','1','0','0','x'],
        ['1','1','1','1','1','1']]
MaxSize = 6

result = smartSearch()
if result:print(' --> 미로탐색 성공!')
else: print(' --> 미로탐색 실패!')

# p190 실습문제 5.3 구현 및 실습 

def p():
    q = CircularQueue()
    print("피보나치 수열 : ",end='')

    q.enqueue(0)
    q.enqueue(1)
    print("0 1 ",end = '')

    for i in range(MAX_QSIZE-1):
        a=q.dequeue()+q.peek()
        q.enqueue(a)
        print(a,end = ' ')

p()