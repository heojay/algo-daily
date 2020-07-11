# Baekjoon Online Judge
# 11058. 크리보드
# https://www.acmicpc.net/problem/11058

'''
원래는 i개의 A를 만들기 위한 최소 클릭 수로 하려고 했는데,
숫자가 너무 커져서 역함수로 바꿨다.
i-2-j의 뜻은 CTRL+A, CTRL+C 기본 2번에 추가로 CTRL+V를 누르는 횟수.
'''

N = int(input())
A = [i for i in range(N+1)]
# A[i] i번 눌러서 나오는 A의 최대 개수

for i in range(N+1):
    j = 1
    while i-2-j >= 0:
        A[i] = max(A[i], A[i-2-j] * (1+j))
        j += 1

print(A[-1])