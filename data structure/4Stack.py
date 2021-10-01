# 1. 스택이란?
    # 후입선출의 자료구조
    # 자료의 삽입과 삭제를 한쪽으로만 하는 선형구조

    # 용도
        # 편집기의 되돌리기
        # 함수호출에서 복귀주소 저장
        # 괄호 검시
        # 계산기
        # 미로 탐색 등
    
# 2. 스택의 구현 : 배열구조, 파이썬의 리스트 사용(후단)

    # 함수 버전

top = [] # 스택 데이터

def isEmpty():
    return len(top) == 0
def push(item):
    top.append(item)
def pop():
    if not isEmpty():
        return top.pop(-1)
def peek():
    if not isEmpty():
        return top[-1]
def size():
    return len(top)
def clear():
    global top
    top = []

    # 클래스 버전

class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top) == 0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def size(self):
        return len(self.top)
    def clear(self):
        self.top = []

    def __str__(self): # 연산자 중복 + 슬라이싱 기법 # a.top로 출력해도 됨
        return str(self.top[::-1]) # 역순 

    # form Stack import *

# 3. 스택의 응용 : 괄호 검사
    # []. {}, ()

def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in('{','[','('):
            stack.push(ch)
        elif ch in ('}',']',')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == '}' and left != '{') or \
                    (ch == ']' and left != '[') or \
                    (ch == ')' and left != '('):
                    return False
    
    return stack.isEmpty()

str = "{ A[i+1] = 0;}"
checkBrackets(str)

    # 소스파일에서 괄호검사

def checkBracketsV2(lines):
    for line in lines:
        res = checkBrackets(line)
        if not res:
            return res

infile = open("C:\\Users\\dhaab\\OneDrive\\문서\\파이썬\\datapy\\1numpy.py","r")
lines = infile.readlines()
infile.close()

print(checkBracketsV2(lines))

# 4. 스택의 응용 : 수식의 계산

    # 전위 +AB
    # 중위 A+B
    # 후위 AB+

    # 계산기 프로그램 만드는 과정: 1. 중위-> 후위 변환 2. 후위 계산

        # 2. 후위 표기 수식 계산 구현 (연산자 +, -, *, /)

# from Stack import *

def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val1 = s.pop()
            val2 = s.pop()
            if token == '+': s.push(val1+val2)
            elif token == '-': s.push(val1-val2)
            elif token == '*': s.push(val1*val2)
            elif token == '-': s.push(val1/val2)
        else:
            s.push(float(token))
    return s.pop()

        # 1. 스택을 이용한 중위표기 수식의 후위표기 변환

def precedence(op): # 연산자들 우선순위
    if op =='(' or op == ')' : return 0
    elif op =='+' or op == '-' : return 1
    elif op =='*' or op == '/' : return 2
    else : return -1

def Infix2Postfix(expr):
    s = Stack()
    output = []
    for t in expr:
        if t in '(':
            s.push('(')
        elif t in ')':
            while not s.isEmpty():
                op = s.push(t)
                if op == '(':
                    break
                else: 
                    output.append(op)
        elif t in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(t)<=precedence(op):
                    output.append(op)
                    s.pop()
                else:break
            s.push(t)
        else : output.append(t)

    while not s.isEmpty():
        output.append(s.pop())

    return output

# + 미로 탐색 & 과제
