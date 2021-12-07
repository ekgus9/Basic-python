# 1. 탐색 트리 란?
    # 이진 탐색 트리: 삽입, 삭제, 탐색 O(log N)
    
# 2. 이진탐색트리의 연산

class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
    # 탐색 key < 노드 key : 왼쪽 서브트리 탐색
    # 탐색 key > 노드 key : 오른쪽 서브트리 탐색
    
def search_bst_iter(n,key): # O(n)
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_max_bst(n): # 오른쪽으로 갈 수록 커짐(왼쪽은 작아짐)
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

    # 삽입 연산 (탐색이 끝나면 삽입)
    
def insert_bst(r,n): # 트리, 삽입 노드
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left,n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right,n)
    else:
        return False
    
    # 삭제 연산
    
    # case1. 단말 노드 삭제
    
def delete_bst_case1(parent,node,root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else: parent.right = None
    return root

    # case2. 자식이 하나인 노드 삭제
    
def delete_bst_case2(parent,node,root):
    if node.left is not None:
        child = node.left
    else: child = node.right
    
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root

    # case3. 두 개의 자식 가진 노드 삭제
        # 가장 비슷한 값 가진 노드 가져옴
        # 후계 노드 선택 : 왼쪽 서브 트리 가장 큰 값이나 오른쪽 가장 큰 값 선택
    
def delete_bst_case3(parent,node,root):
    succp = node
    succ = node.right
    while succ.left != None:
        succp = succ
        succ = succ.left
    
    if succp.left == succ:
        succp.left = succ.right
    else:
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value
    node = succ
    
    return root

    # 종합 삭제 코드
    
def delete_bst (root, key):
    if root == None: return None
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else: node = node.right
        
    if node == None: return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent,node,root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent,node,root)
    else:
        root = delete_bst_case3(parent,node,root)
    return root

# 3. 이진탐색 트리를 이용한 맵

def count_node(n): # 8Tree.py
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
    
def inorder(n): # 중위 순회
    if n is not None:
        inorder(n.left)
        print(n.key,end=' ')
        inorder(n.right)

class BSTMap():
    def __init__(self):
        self.root = None
    def isEmpty(self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root)
    def search(self,key): return search_bst_iter(self.root,key)
    def findMax(self): return search_max_bst(self.root)
    def findMin(self): return search_min_bst(self.root)
    
    def insert(self,key,value=None):
        n = BSTNode(key,value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root,n)
    def delete(self,key):
        self.root = delete_bst(self.root,key)
    def display(self,msg='BSTMap:'):
        print(msg,end='')
        inorder(self.root)
        print()
        
map = BSTMap()
data = [35,18,7,26,12,3,68,22,30,99]
print("[삽입 연산] : ", data)
for key in data:
    map.insert(key)
map.display("[중위 순회] : ")
    
if map.search(26) != None : print('[탐색 26 ]: 성공')
else: print('[탐색 26 ]: 실패')
if map.search(25) != None : print('[탐색 25 ]: 성공')
else: print('[탐색 25 ]: 실패')

map.delete(3)
map.display("[3 삭제] : ")
map.delete(68)
map.display("[68 삭제] : ")
map.delete(18)
map.display("[18 삭제] : ")
map.delete(35)
map.display("[35 삭제] : ")

# 4. 심화 학습: 균형탐색이진트리 AVL
    # 항상 균형 트리 보장: 비균형 상태가 되면 노드 재배치
    # 균형 인수: 왼쪽 서브 트리 높이 - 오른 쪽 서브 트리 높이 (0,1,-1)
    # O(log n) 보장
    
    # 탐색연산은 이진 트리와 동일
    # 삽입, 삭제 시 균형 깨질 수 있음 -> 재배열 필요
    # 삽입 연산 -> 불균형 -> 균형인수가 +-2가 된 가장 가까운 조상노드의 서브 트리에 대해여 재균형
    
    # LL회전

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

    # RR회전
    
def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

    # RL회전
    
def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

    # LR회전
    
def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

    # 재균형 함수
    
def calc_height(n):
    if n == None: return 0
    hleft = calc_height(n.left)
    hright = calc_height(n.right)
    return max(hleft,hright) + 1 
    
def calc_height_diff(n):
    if n == None: return 0
    return calc_height(n.left) - calc_height(n.right)
    
def reBalance(parent):
    hDiff = calc_height_diff(parent)
    if hDiff>1:
        if calc_height_diff(parent.left)>0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff<-1:
        if calc_height_diff(parent.right)<0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

    # 삽입 함수
    
def insert_avl(parent,node):
    if node.key<parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left,node)
        else:
            parent.left = node
        return reBalance(parent)
    elif node.key>parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right,node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")

# from BSTMap import *

def levelorder(n):
    que = []
    que.append(n)
    while len(que) != 0:
        node = que.pop(0)
        if node is not None:
            print(node.key,end=' ')
            que.append(node.left)
            que.append(node.right)

def count_leaf(n):
    if n is None: return 0
    elif n.left is None and n.right == None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

class AVLMap(BSTMap):
    def __init__(self):
        super().__init__() 
    def insert(self,key,value=None):
        n=BSTNode(key,value)
        if self.isEmpty(): self.root = n
        else: self.root = insert_avl(self.root,n)
        
    def display(self,msg='AVLMap: '):
        print(msg,end='')
        levelorder(self.root)
        print()
        
node = [7,8,9,2,1,5,3,6,4]
map = AVLMap()
for i in node :
    map.insert(i)
    map.display("AVL(%d): "%i)
print("노드의 개수 = %d"%count_node(map.root))
print("단말의 개수 = %d"%count_leaf(map.root))
print("트리의 높이 = %d"%calc_height(map.root))