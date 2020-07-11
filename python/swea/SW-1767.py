# SW Expert Academy
# 1767. [SW Test 샘플문제] 프로세서 연결하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

'''
가능한 경우를 모두 확인한다.
첫 번째 코어부터 4방향 모두 확인하는 것이 필요하다.
다 탐색하면 기존의 탐색 결과와 비교해준다.
여기에 효율을 위해서앞으로 남은 모든 코어를 다 연결해도,
더 많은 코어를 연결할 수 없다면 더 이상 탐색하지 않는 것을 포함한다.
'''

def isLine(x, y, dir): # Line을 그릴 수 있는지 확인하는 부분
    global N

    if(dir == 0):
        for i in range(0, x):
            if(MAP[i][y] != 0):
                return False
    elif(dir == 1):
        for i in range(x+1, N):
            if(MAP[i][y] != 0):
                return False
    elif(dir == 2):
        for i in range(0, y):
            if(MAP[x][i] != 0):
                return False
    elif(dir == 3):
        for i in range(y+1, N):
            if(MAP[x][i] != 0):
                return False
    return True

def drawLine(x, y, dir): # Line을 그리는 부분
    global N
    length = 0

    if(dir == 0):
        for i in range(0, x):
            MAP[i][y] = 2
            length += 1
    elif(dir == 1):
        for i in range(x+1, N):
            MAP[i][y] = 2
            length += 1
    elif(dir == 2):
        for i in range(0, y):
            MAP[x][i] = 2
            length += 1
    elif(dir == 3):
        for i in range(y+1, N):
            MAP[x][i] = 2
            length += 1
    return length

def clearLine(x, y, dir): # Line을 지우는 부분
    global N

    if(dir == 0):
        for i in range(0, x):
            MAP[i][y] = 0
    elif(dir == 1):
        for i in range(x+1, N):
            MAP[i][y] = 0
    elif(dir == 2):
        for i in range(0, y):
            MAP[x][i] = 0
    elif(dir == 3):
        for i in range(y+1, N):
            MAP[x][i] = 0
    return

def DFS(idx, p, line):
    global MAXP, MINL, CORE

    if(len(CORE)-idx+p < MAXP): # 앞으로 남은 모든 코어를 다 연결해도 작다면 
        return
    
    if(idx == len(CORE)): # 모든 코어의 연결 상태를 다 확인했다면
        if(MAXP < p): # 현재 코어가 가장 많은 코어라면
            MINL = line
            MAXP = p
        elif(MAXP == p and MINL > line): # 같다면, line 개수를 다르게
            MINL = line
    else:
        x, y = CORE[idx]
        for i in range(4):
            if(isLine(x, y, i)): # 만약 가로막는 장애물이 없다면
                DFS(idx + 1, p + 1, line + drawLine(x, y, i)) # 새로 그리고 더 확인
                clearLine(x, y, i) # 다 확인 했으면 지우고
        DFS(idx + 1, p, line) # 그리지 않고 다음 CORE로 이동
    return
            
for test in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    CORE = []
    for i in range(N):
        for j in range(N):
            if(MAP[i][j]):
                CORE.append((i,j))
    MAXP = -1
    MINL = 9999
    DFS(0, 0, 0)
    print('#' + str(test+1) + ' ' +str(MINL))