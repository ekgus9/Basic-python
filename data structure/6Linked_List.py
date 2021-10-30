# 1. 연결된 구조 : 흩어진 데이터를 링크로 연결하여 관리
    # 노드 = 데이터 + 링크

    # 용량 고정 x
    # 삽입, 삭제 용이 O(1)
    # n번째 항목 접근 시간 걸림 O(n)

    # 헤드포인터 : 첫 노드 주소 저장

# 2. 단순연결리스트 응용 : 연결된 스택

class Node:
    def __init__(self,elem, link = None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self): return self.top == None
    def clear(self): self.top = None

    def push(self,item):
        n = Node(item,self.top)
        self.top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def size(self):
        n=self.top
        count = 0
        while not n == None:
            n = n.link
            count += 1
        return count
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    def display(self,msg='LinkedStack : '):
        print(msg,end="")
        node = self.top
        while not node ==None:
            print(node.data,end='')
            node = node.link
        print()

# 3. 단순 연결 리스트 응용 : 연결 리스트 (임의 위치 삽입, 삭제)

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self):
        node = self.head
        while not node == None:
            print(node.data,end='')
            node = node.link
    def getNode(self,pos):
        if pos<0: return None
        node = self.head
        while pos>0 and node != None:
            node = node.link
            pos -= 1
        return node
    def getEntry(self,pos):
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data
    def replace(self,pos,elem):
        node = self.getNode(pos)
        if not node == None:
            node.data = elem
    def find(self,data):
        node = self.head
        while node is not None:
            if node.data == data: return node
            node = node.link
        return node
    def insert(self,pos,elem):
        before = self.getNode(pos-1)
        if before == None: self.head = Node(elem,self.head)
        else:
            node = Node(elem,before.link)
            before.link = node
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
            elif before.link != None:
                before.link = before.link.link

# 4. 원형 연결 리스트의 응용 : 연결된 큐

class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None
    def peek(self): 
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self,item):
        node = Node(item,None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail: self.tail = None
            else: self.tail.link = self.tail.link.link
            return data
    def size(self):
        if self.isEmpty(): return 0
        else: 
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count
    def display(self,msg='CircularLinkedQueue:'):
        print(msg,end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data,end ='')
                node = node.link
            print(node.data,end='')
        print()

# 5. 이중 연결 리스트의 응용 : 연결된 덱
    # 단순 연결 리스트 덱은 후단 삭제시 O(n)

class DNode:
    def __init__(self,elem,prev=None,next=None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self): return self.front == None
    def clear(self): self.front = self.rear = None
    def size(self):
        count = 0
        node = self.front
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self,msg):
        node = self.front
        while not node == None:
            print(node.data, end='')
            node = node.link
    def addFront(self,item):
        node = DNode(item,None,self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
    def addrear(self,item):
        node = DNode(item,self.rear,None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else: 
                self.front.prev = None
            return data
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else: 
                self.rear.next = None
            return data


# P233 실습문제 6.3번 구현 및 실습 -> 단순 연결 리스트 큐

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self): return self.front == None
    def clear(self): self.front = self.rear = None
    def peek(self): 
        if not self.isEmpty():
            return self.front.data
    def enqueue(self,item):
        node = Node(item,None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            if self.front.link == None: self.front = self.rear = None
            else: self.front = self.front.link
            return data
    def size(self):
        if self.isEmpty(): return 0
        else: 
            count = 1
            node = self.front
            while not node == self.rear:
                node = node.link
                count += 1
            return count
    def display(self,msg='CircularLinkedQueue: '):
        print("size:",self.size())
        print(msg,end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data,end =' ')
                node = node.link
            print(node.data,end='')
        print()

lq = LinkedQueue()

print("0~7 정수 큐에 삽입")
for i in range(0,8): lq.enqueue(i)
lq.display()

print("\n큐에서 4개 삭제")
for i in range(4): lq.dequeue()
lq.display()

print("\n8~13 정수 큐에 삽입")
for i in range(8,14): lq.enqueue(i)
lq.display()
