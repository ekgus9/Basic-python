# 1. 큐란?
    # 선입선출 자료구조 -> 삽입 후단, 삭제 전단

# 2. 큐의 구현

    # 선형큐 비효율적 : 삭제할때 모든 요소 앞으로 이동 O(n)

    # 원형큐 효율적 O(1)
        # 리스트 고정
        # front(최근 삭제 위치) , rear(최근 삽입 위치)

    # 공백 상태: front == rear
    # 변수 증가: front = (front+1)%MAX_QSIZE, rear = (rear+1)%MAX_QSIZE
    # 포화 상태: front == (rear+1)%MAX_QSIZE

    # 원형 큐의 구현

MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE
    
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear + 1)%MAX_QSIZE
    def clear(self):
        self.front = self.rear
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE)%MAX_QSIZE
    def display(self):
        out=[]
        if(self.front<self.rear):
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s,r=%d]==>"%(self.front,self.rear),out)

q=CircularQueue()
for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.dequeue()
q.display()
for i in range(8,14): q.enqueue(i)
q.display()

# 3. 큐의 응용 : 너비우선탐색 (BFS)
    # 인접 위치 방문 -> 모든 경우 가보기
def isValidPos(x,y):
    if x<0 or y<0 or x>=MaxSize or y>=MaxSize:
        return False
    else:
        return map[x][y]=='0' or  map[x][y]=='x'

def BFS():
    que = CircularQueue()
    que.enqueue((1,0))
    print('BFS:')

    while not que.isEmpty():
        here = que.dequeue()
        x,y = here
        print(here,end='->')
        if map[x][y] == 'x': return True
        else:
            map[x][y]='.'
            if isValidPos(x-1,y): que.enqueue((x-1,y))
            if isValidPos(x+1,y): que.enqueue((x+1,y))
            if isValidPos(x,y-1): que.enqueue((x,y-1))
            if isValidPos(x,y+1): que.enqueue((x,y+1))

map = [['1','1','1','1','1','1'],
        ['e','0','1','0','0','1'],
        ['1','0','0','0','1','1'],
        ['1','0','1','0','1','1'],
        ['1','0','1','0','0','x'],
        ['1','1','1','1','1','1']]
MaxSize = 6

result = BFS()
if result:print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')

    # 파이썬의 queue 모듈

import queue

Q = queue.Queue(maxsize=20) # 큐 객체 생성

for i in range(1,10):
    Q.put(i) # 삽입
print("큐의 내용: ",end='')
for i in range(1,10):
    print(Q.get(),end=' ') # 삭제


# + 덱 , 우선순위 큐