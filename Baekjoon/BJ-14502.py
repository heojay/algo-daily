# Baekjoon Online Judge
# 14502. 연구소
# https://www.acmicpc.net/problem/14502

'''
아무리해도 연산이 너무 오래 걸려서 고민했던 문제..
wall을 고르는 방법을 조합이 아닌 순열로 한 탓이었다.
'''

import copy

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(M):
        if(MAP[i][j] == 2):
            virus.append((i, j))

ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_dfs(v0, v1, nMAP):
    for i in range(4):
        nx, ny = v0 + dx[i], v1 + dy[i]
        if(nx < N and nx >= 0 and ny < M and ny >= 0):
            if(nMAP[nx][ny] == 0):
                nMAP[nx][ny] = 2
                spread_dfs(nx, ny, nMAP)

def dfs(wall, start):
    global ans
    if(len(wall) == 3):
        nMAP = copy.deepcopy(MAP)
        for w in wall:
            nMAP[w[0]][w[1]] = 1

        for v in virus:
            spread_dfs(v[0], v[1], nMAP)

        safe = 0

        for i in range(N):
            for j in range(M):
                if(not nMAP[i][j]):
                    safe += 1
        
        ans = max(ans, safe)
        return

    else:
        si = start // N
        for i in range(si, N):
            for j in range(M):
                if(not MAP[i][j] and (i,j) not in wall):
                    wall.append((i,j))
                    dfs(wall, i*N)
                    wall.pop()

dfs([], 0)

print(ans)