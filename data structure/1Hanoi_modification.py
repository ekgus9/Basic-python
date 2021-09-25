    # 하노이 탑 과제
        # A 막대의 원판을 모두 C 막대로 옮기기 (B 임시 막대)
        # 한 번에 원판 하나씩
        # 반드시 큰 판 위 작은 판
        # + 총 이동 횟수 추가
        # + 한 프로그램에서 n = 1, 2, 3, 4 일 때 모두 실행

def hanoi(i, fr, tmp, to):

    global count
    
    if (i == 1):
        print("원판 1: %s --> %s" % (fr, to))
        count += 1
    else :
        hanoi(i-1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (i, fr, to))
        count += 1
        hanoi(i-1, tmp, fr, to)
    
for i in range(1, 5):   
    
    count = 0
    
    hanoi(i, "A", "B", "c")

    print("총횟수 : ", count)
    print("================")
