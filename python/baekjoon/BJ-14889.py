# Baekjoon Online Judge
# 14889. 스타트와 링크
# https://www.acmicpc.net/problem/14889

'''
모든 경우를 다 하면 된다.
NC(N//2) 라는 것을 이용해서 Combination을 이용해도 된다.
'''

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

MIN = 100000000

def dfs(mem, idx, num):
    global MIN
    if idx == N:
        smem = []
        lmem = []
        for i in range(N):
            if mem[i] == '1':
                smem.append(i)
            else:
                lmem.append(i)
        start = sum([S[i][j] for i in smem for j in smem])
        link = sum([S[i][j] for i in lmem for j in lmem])
        MIN = min(abs(start-link), MIN)
        return
    if num == N//2:
        dfs(mem+'0', idx+1, num)
    elif idx - num == N//2:
        dfs(mem+'1', idx+1, num+1)
    else:
        dfs(mem+'0', idx+1, num)
        dfs(mem+'1', idx+1, num+1)

dfs("", 0, 0)

print(MIN)