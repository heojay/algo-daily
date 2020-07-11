# Baekjoon Online Judge
# 2169. 로봇 조종하기
# https://www.acmicpc.net/problem/2169

'''
직전에 어느 방향에서 왔는 지 고려하는 방식으로 푼다.
'''

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
val = [[0 for _ in range(M)] for __ in range(N)]

val[0][0] = MAP[0][0]

for i in range(1,M):
    val[0][i] = val[0][i-1] + MAP[0][i]

for i in range(1,N):
    up = [0] * M
    left = [0] * M
    right = [0] * M
    for j in range(M):
        up[j] = val[i-1][j] + MAP[i][j] # 위에서 내려오는 경우
    
    left[0] = val[i-1][0] + MAP[i][0]
    right[-1] = val[i-1][-1] + MAP[i][-1]
    for j in range(1, M):
        left[j] = max(left[j-1] + MAP[i][j], up[j]) # 왼쪽에서 오는 경우
    for j in range(2, M+1):
        right[-j] = max(right[-j+1] + MAP[i][-j], up[-j]) # 오른쪽에서 오는 경우

    for j in range(M):
        val[i][j] = max(left[j], right[j], up[j])
    
print(val[-1][-1])