# Baekjoon Online Judge
# 17135. 캐슬 디펜스
# https://www.acmicpc.net/problem/17135

'''
이 풀이의 의의.
모르겠다..

'''

def dfs(n, idx, pos):
    global N, M, D, ans
    if(idx != 3 and n == M):
        return
    if(idx == 3):
        temp = 0
        kill = [[-1 for _ in range(M)] for __ in range(N)]
        for i in range(N):
            for p in pos:
                flag = False
                for j in range(1, D+1):
                    for k in range(j+1):
                        if N-i-k < 0 or N-i-k >= N or p-j+k >= M or p-j+k < 0:
                            continue
                        if MAP[N-i-k][p-j+k]:
                            if(kill[N-i-k][p-j+k] != -1):
                                if(kill[N-i-k][p-j+k] != i):
                                    continue
                                else:
                                    flag = True
                                    break
                            else:
                                kill[N-i-k][p-j+k] = i
                                temp += 1
                                flag = True
                                break
                    if(flag):
                        break

                    for k in range(j,-1,-1):
                        if N-i-k < 0 or N-i-k >= N or p+j-k >= M or p+j-k < 0:
                            continue
                        if MAP[N-i-k][p+j-k]:
                            if(kill[N-i-k][p+j-k] != -1):
                                if(kill[N-i-k][p+j-k] != i):
                                    continue
                                else:
                                    flag = True
                                    break
                            else:
                                kill[N-i-k][p+j-k] = i
                                temp += 1
                                flag = True
                                break
                    if(flag):
                        break
            for t in range(M):
                if(kill[N-i-1][t] == -1):
                    kill[N-i-1][t] = -2

        ans = max(ans, temp)
        return
    pos.append(n)
    dfs(n+1, idx+1, pos)
    pos.pop()
    dfs(n+1, idx, pos)
    return
    
ans = 0
N, M, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dfs(0,0,[])
print(ans)