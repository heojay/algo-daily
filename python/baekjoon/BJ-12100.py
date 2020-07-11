# Baekjoon Online Judge
# 12100. 2048 (Easy)
# https://www.acmicpc.net/problem/12100

'''
1. 진법을 구현해서 모든 move를 돌려고 했더니 시간초과가 나왔다. DFS가 더 빠른듯.
2. 지도를 list로 구현하니 주소 문제가 자꾸 발목을 잡았다.
객체를 새로 정의하는 dir 1,0은 그냥 넘어갔지만,
dir 2,3은 세로에 하나 하나 새로 넣는 형태라서 문제가 됐다.
결국 deepcopy로 해결했다.
3. 구현 자체는 queue로 간단하게 구현할 수 있다.
'''


import queue
import copy

def merge(l):
    q = queue.Queue()
    for i in range(len(l)):
        q.put(l[i])
    a = []
    now = 0
    while q.qsize():
        x = q.get()
        if(x == 0):
            continue
        elif(now == 0):
            now = x
            continue
        elif(now == x):
            a.append(2*x)
            now = 0
        else:
            a.append(now)
            now = x
    if(now != 0):
        a.append(now)
    for i in range(len(l) - len(a)):
        a.append(0)
    return a

def move(MOVE_MAP, N, dir):
    if(dir == 0): # 왼쪽
        for i in range(N):
            MOVE_MAP[i] = merge(MOVE_MAP[i])

    if(dir == 1): # 오른쪽
        for i in range(N):
            MOVE_MAP[i] = merge(MOVE_MAP[i][::-1])[::-1]
    
    if(dir == 2): #위
        for i in range(N):
            temp = [MOVE_MAP[j][i] for j in range(N)]
            temp = merge(temp)
            for j in range(N):
                MOVE_MAP[j][i] = temp[j]
    
    if(dir == 3): #아래
        for i in range(N):
            temp = [MOVE_MAP[-j][i] for j in range(1,N+1)]
            temp = merge(temp)
            for j in range(1,N+1):
                MOVE_MAP[-j][i] = temp[j-1]
                
    return


N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

MAX = 0

def dfs(MAP, N, now):
    global MAX
    if(now == 5):
        temp = max([max(MAP[i]) for i in range(N)])
        MAX = max(MAX, temp)
        return
    else:
        for i in range(4):
            nMAP = copy.deepcopy(MAP)
            move(nMAP, N, i)
            dfs(nMAP, N, now+1)

dfs(MAP, N, 0)

print(MAX)