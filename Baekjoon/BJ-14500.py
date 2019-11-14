# Baekjoon Online Judge
# 14500. 테트리미노
# https://www.acmicpc.net/problem/14500

'''
1. 뒤돌아가지 않는 테트리미노 (I, O, Z, S, J, L미노)
2. T미노
로 나뉘어서 합을 찾는다. 최대한 합 연산을 덜 하도록 노력했다.
'''

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def dfs(block, S):
    global ans
    if(len(block) == 4):
        ans = max(ans, S)
        return
    else:
        for dir in [(0,1), (0,-1), (1,0)]:
            nx, ny = block[-1][0]+dir[0], block[-1][1]+dir[1]
            if(nx >= 0 and nx < N and ny >= 0 and ny < M):
                if((nx, ny) not in block):
                    block.append((nx, ny))
                    S += MAP[nx][ny]
                    dfs(block, S)
                    block.pop()
                    S -= MAP[nx][ny]

for i in range(N):
    for j in range(M):
        dfs([(i,j)], MAP[i][j])

for i in range(N):
    for j in range(M):
        if(i > 0 and i < N-1):
            if(j > 0 and j < M-1):
                cross = MAP[i][j] + MAP[i][j+1] + MAP[i][j-1] + MAP[i+1][j] + MAP[i-1][j]
                ans = max(ans, cross-MAP[i][j+1])
                ans = max(ans, cross-MAP[i][j-1])
                ans = max(ans, cross-MAP[i+1][j])
                ans = max(ans, cross-MAP[i-1][j])
            else:
                if(j == 0):
                    ans = max(ans, MAP[i-1][j] + MAP[i][j+1] + MAP[i][j] + MAP[i+1][j])
                elif(j == M-1):
                    ans = max(ans, MAP[i-1][j] + MAP[i][j-1] + MAP[i][j] + MAP[i+1][j])
        elif(j > 0 and j < M-1):
            if(i == 0):
                ans = max(ans, MAP[i][j-1] + MAP[i][j] + MAP[i+1][j] + MAP[i][j+1])
            elif(i == N-1):
                ans = max(ans, MAP[i][j-1] + MAP[i][j] + MAP[i-1][j] + MAP[i][j+1])

print(ans)