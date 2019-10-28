# Baekjoon Online Judge
# 17471. 게리멘더링
# https://www.acmicpc.net/problem/17471

'''
16일 SW Expert 시험에 응시했으니 기출 문제 위주로 풀어보기로 했음.
처음에 무식하게 뭐라도 연결되어있으면 valid라고 했는데 섬처럼 떨어져있는 경우가 있어서..
find 부분을 하나로 줄일 수도 있을듯...
'''


N = int(input())
P = [0] + list(map(int, input().split()))
C = {}
for i in range(N):
    C[i+1] = list(map(int, input().split()))[1:]

MIN = 999999

for i in range(1, 2**N-1):
    w = bin(i)[2:]
    temp = list((N-len(w)) * '0' + w)
    A = []
    B = []
    for i in range(N):
        if(temp[i] == '0'):
            A.append(i+1)
        else:
            B.append(i+1)
    
    valid = True

    seen = [False] * (N+1)
    find = [A[0]]

    while find:
        now = find.pop()
        seen[now] = True
        for NEXT in C[now]:
            if(NEXT in A and not seen[NEXT]):
                find.append(NEXT)
    for i in A:
        if(not seen[i]):
            valid = False

    seen = [False] * (N+1)
    find = [B[0]]

    while find:
        now = find.pop()
        seen[now] = True
        for NEXT in C[now]:
            if(NEXT in B and not seen[NEXT]):
                find.append(NEXT)
    for i in B:
        if(not seen[i]):
            valid = False
   
    if(not valid):
        continue

    sumA = sum(P[i] for i in A)
    sumB = sum(P[i] for i in B)

    MIN = min(abs(sumA - sumB), MIN)

if(MIN == 999999):
    print(-1)
else:
    print(MIN)