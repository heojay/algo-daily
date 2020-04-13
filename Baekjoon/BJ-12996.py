# Baekjoon Online Judge
# 12996. Acka
# https://www.acmicpc.net/problem/12996

'''
탑-다운 방식의 DP 문제. 처음에 반대로 풀려다가 실패.
이항정리를 이용한 풀이가 있는 듯 하다. 추후 업데이트.
'''

S, a, b, c = map(int, input().split())
dp = [[[[-1 for _ in range(c+1)] for __ in range(b+1)] for ___ in range(a+1)] for ____ in range(S+1)]

def sing(S, a, b, c):
    if S == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    elif a < 0 or b < 0 or c < 0:
        return 0
    else:
        if dp[S][a][b][c] != -1:
            return dp[S][a][b][c]
        else:
            dp[S][a][b][c] = 0
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        if i+j+k != 0:
                            dp[S][a][b][c] += sing(S-1, a-i, b-j, c-k)
            dp[S][a][b][c] %= 1000000007
            return dp[S][a][b][c]

print(sing(S,a,b,c))