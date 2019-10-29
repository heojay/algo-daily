# Baekjoon Online Judge
# 17070. 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070

'''
끝점이 어딘지, 지금 자세가 어떤지만 보기로 하자.
사실 저 부분을 Flag같은걸로 처리하면 될거 같긴하지만...
'''

n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
ANS = [[[0,0,0] for _ in range(n)] for __ in range(n)]

ANS[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if(j+1 != n and MAP[i][j+1] != 1):
            ANS[i][j+1][0] += ANS[i][j][0] + ANS[i][j][2]
        if(i+1 != n and MAP[i+1][j] != 1):
            ANS[i+1][j][1] += ANS[i][j][1] + ANS[i][j][2]
        if(i+1 != n and MAP[i+1][j] != 1 and j+1 != n and MAP[i][j+1] != 1 and MAP[i+1][j+1] != 1):
            ANS[i+1][j+1][2] += ANS[i][j][0] + ANS[i][j][1] + ANS[i][j][2]

print(sum(ANS[n-1][n-1]))