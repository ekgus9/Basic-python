# 1. 트리
    # 계층적인 자료의 표헌에 적합한 자료구조
    
    # 루트 노드: 맨 위 하나의 노드
    # 부모/자식 노드
    # 리프(단말) 노드: 자식 없는 노드 <-> 비단말노드
    # 트리 차수 3 2 1 0
    # 트리 높이(레벨) 4 3 2 1
    # 간선 n-1개

# 2. 이진 트리
    # 모든 노드가 2개의 서브 트리 갖는 트리
    # 순환적(재귀함수의 개념/ 서브트리도 이진 트리)
    # 공집합이거나 루트와 왼쪽 서브 트리, 오른쪽 서브 트리로 구성된 노드들 집합
    
    # 포화 이진 트리
        # 트리의 각 레벨에 노드가 꽉 차있는 이진 트리 (2h-1개 노드)
        
    # 완전 이진 트리 (포화 이진 트리를 포함함)
        # 레벨 1부터 h-1까지는 노드가 모두 채워지고
        # 마지막 레벨 h에서는 노드가 순서대로 채워짐
        
    # 편향 이진 트리
    
    # 표현
        # 배열 표현법
            # 완전 이진 트리에 숫자 붙여서 리스트로 표현하기 편리
            # 노드 i의 부모 노드 인덱스 i//2
            # 노드 i의 왼쪽 자식 노드 인덱스 2i
            # 노드 i의 오른쪽 자식 노드 인덱스 2i+1
            
        # 링크 표현법 (화살표 없는 리스트는 None 가짐)
        
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
        
# 3. 이진트리의 연산
    # 순회 traversal
        # 트리에 속하는 모든 노드를 한 번씩 방문
        # 선형 자료구조는 순회 단순
        
        # 전위 순회 (부모 먼저)

def preorder(n):
    if n is not None:
        print(n.data,end=' ')
        preorder(n.left)
        preorder(n.right)
        
        # 중위 순회 (부모 중간)
    
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data,end=' ')
        inorder(n.right)
        
        # 후위 순회 (부모 마지막)
    
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data,end=' ')
        
        # 레벨 순회 (큐 사용)
    
from Queue import *

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data,end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
            
    # 노드 개수
    
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

    # 단말 노드 수
    
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left)+count_leaf(n.right)
    
    # 트리 높이
    
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else: return hRight + 1
    
    # 실행
    
d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',f,None)
root = TNode('A',b,c)

print('\nIn-Order : ',end='')
inorder(root)
print('\nPre-Order : ',end='')
preorder(root)
print('\nPost-Order : ',end='')
postorder(root)
print('\nLevel-Order : ',end='')
levelorder(root)
print()
print("노드의 개수 = %d개"%count_node(root))
print("단말의 개수 = %d개"%count_leaf(root))
print("트리의 높이 = %d"%calc_height(root))

# 4. 이진트리의 응용 : 모르스 코드 결정트리
    # 모르스 부호 : 도트와 대시의 조합으로 구성된 메시지 전달 부호
        # 인코딩 O(1) , 디코딩 O(n)
    
    # 결정트리 : 여러 단계의 복잡한 조건을 갖는 문제에 대한 조건과 해결 방법을 트리 형태로 나타낸 것
        # 디코딩 O(log2n)
        
table = [('A','.-'),('B','-...'),('C','-.-.'),('D','-..'),('E','.'),('F', '..-.'),('G','--.'),('H','....'),('I','..'),('J','.---'),
         ('K','-.-'),('L','.-..'),('M','--'),('N','-.'),('O','---'),('P','.--.'),('Q','--.-'),('R','.-.'),('S','...'),
         ('T','-'),('U','..-'),('V','...-'),('W','.--'),('X','-..-'),('Y','-.--'),('Z','--..')]

def make_morse_tree():
    root = TNode(None,None,None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = TNode(None,None,None)
                node = node.left
            elif c == '-':
                if node.right == None:
                    node.right = TNode(None,None,None)
                node = node.right
        node.data = tp[0]
    return root

def decode(root,code):
    node = root
    for ch in code:
        if ch == '.': node = node.left
        elif ch == '-': node = node.right
    return node.data

def encode(ch):
    idx = ord(ch)-ord('A')
    return table[idx][1]

morseCodeTree = make_morse_tree()
str1 = input("입력 문장 : ")
mlist = []
for ch in  str1:
    code = encode(ch)
    mlist.append(code)
print("Morse Code : ",mlist)
print("Decoding : ",end='')
for code in mlist:
    ch = decode(morseCodeTree,code)
    print(ch,end='')

# 5. 힙트리
    # 완전이진트리 기반
    # 가장 큰(or 작은) 값 빠르게 찾기 위한 지료구조 -> 느슨한 정렬 상태
    # 최대 힙(부모 노드 키 값이 자식보다 크거나 같은 완전이지트리), 최소 힙(작거나 같은)
    
    # 삽입
        # Upheap -> O(log2n) : 새로운 항목을 힙의 마지막 노드 다음 위치에 삽입
        
    # 삭제
        # Downheap -> O(log2n) : 루트 노드 삭제 후 빈 자리에 마지막 노드 가져옴(->내림)
        
    # 배열로 구현
    
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)
    def size(self): return len(self.heap)-1
    def isEmpty(self): return self.size() == 0
    def Parent(self,i): return self.heap[i//2]
    def Left(self,i): return self.heap[i*2]
    def Right(self,i): return self.heap[i*2+1]
    def display(self,msg='힙 트리: '):
        print(msg,self.heap[1:])
    def insert(self,n):
        self.heap.append(n)
        i = self.size()
        while i != 1 and n>self.Parent(i):
            self.heap[i] = self.Parent(i)
            i=i//2
        self.heap[i] = n
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while child <= self.size():
                if child<self.size() and self.Left(parent)<self.Right(parent):
                    child+=1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent=child
                child*=2
            self.heap[parent]=last
            self.heap.pop(-1)
            return hroot
        
heap = MaxHeap()
data = [2,5,4,8,9,3,7,3]
print("[삽입 연산] : "+str(data))
for elem in data:
    heap.insert(elem)
heap.display('[ 삽입 후 ]: ')
heap.delete()
heap.display('[ 삭제 후 ]: ')
heap.delete()
heap.display('[ 삭제 후 ]: ')

# 6. 힙의 응용: 허프만 코드
    # 문자 빈도따라 다른 길이
    
def make_tree(freq):
    heap=MinHeap()
    for n in freq:
        heap.insert(n)
    for i in range(0,n):
        e1=heap.delete()
        e2=heap.delete()
        heap.insert(e1+e2)
        print(" (%d+%d)"%(e1,e2))
        
label = ['E','T','N','I','S']
freq = [15,12,8,6,4]
make_tree(freq)