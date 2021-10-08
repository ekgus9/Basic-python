# 5. 스택의 응용 : 미로 탐색

    # 깊이우선탐색 (DFS)
        # 가던 길이 막히면 가장 최근 갈림길로 돌아가서 선택하지 않았던 길 선택
        # 갈림길 스택에 저장

    # 1) 시작 위치 스택에 넣음
    # 2) 스택 공백 아니면 위치 하나 꺼냄
        # 현재위치 '.' 표시
        # 스택 공백이면 출구 없음
    # 3) 출구면 탐색 종료
    # 4) 상하좌우 방 중 갈 수 있는 방 스택 저장 -> 2

from Stack import *

def isValidPos(x,y):
    if x<0 or y<0 or x>=MaxSize or y>=MaxSize:
        return False
    else:
        return map[x][y]=='0' or  map[x][y]=='x'
    
def DFS():
    stack = Stack()
    stack.push((1,0))
    print('DFS: ')

    while not stack.isEmpty():
        here=stack.pop()
        print(here,end='->')
        (x,y) = here
        if map[x][y]=='x':
            return True
        else:
            map[x][y]='.'
            if isValidPos(x-1,y):stack.push((x-1,y))
            if isValidPos(x+1,y):stack.push((x+1,y))
            if isValidPos(x,y-1):stack.push((x,y-1))
            if isValidPos(x,y+1):stack.push((x,y+1))

        print("현재스택:",stack)

    return False

map = [['1','1','1','1','1','1'],
        ['0','0','0','0','0','1'],
        ['1','0','1','0','1','1'],
        ['1','1','1','0','0','x'],
        ['1','1','1','0','1','1'],
        ['1','1','1','1','1','1']]
MaxSize = 6

result = DFS()
if result:print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')

# 과제 : 휘문체크 구현 및 실현
    # 입력한 문자 소문자로 변환
    # 스택에서 꺼낸 문자를 저장된 문자열 앞쪽부터 비교

import math

def check():
    stack = Stack()
    lst = []
    strS = list(str) # 한글자씩 나눠주기
    for i in strS:
        if i.isalpha():
            lst.append(i.lower())
            
    global pr
    pr = "".join(lst)

    for i in range(math.ceil(len(lst)/2),len(lst)): 
        stack.push(lst[i])
    
    count = 0
    while count <= math.floor(len(lst)/2)-1: 
        if lst[count] != stack.pop():
            return False
        count+=1
    return True

str = input("회문 체크용 문자열 : ")

result = check()
if result: print('%s : 회문임!!'%pr)
else: print('%s : 회문아님!!'%pr)
