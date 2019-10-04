# SW Expert Academy
# 1247. [S/W 문제해결 응용] 3일차 - 최적 경로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD&categoryId=AV15OZ4qAPICFAYD&categoryType=CODE

'''
저번 문제에 이어 이번에도 DFS.
방문 가능한 모든 순서를 찾아주면 된다.
중간에 지금까지보다 길어지면 pass 하는걸로.
10! = 3628800이기 때문에 가능한 일.
'''

def calDist(a, b): # 거리를 계산하는 함수
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def dfs(rest, last, dist): # 남은 거, 마지막으로 들러서 앞으로 출발할 출발점, 지금까지 거리.
    global minDist, company, home, client
    if(dist > minDist): # 이미 이전에 구한 최소거리보다 길면 pass.
        return
    elif(len(rest) == n): # 시작할 때
        for i in range(n):
            now = rest[i]
            dfs(rest[:i]+rest[i+1:], now, dist + calDist(company, client[now]))
    elif(not rest): # 끝날 때
        dist += calDist(home, client[last])
        minDist = min(minDist, dist)
        return
    else:
        for i in range(len(rest)): # 이번에 거리를 구할 걸 제외하고 다시 탐색.
            now = rest[i]
            dfs(rest[:i]+rest[i+1:], now, dist + calDist(client[last], client[now]))

for test in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    
    minDist = 3000 # 최악의 경우, 0,0과 100,100을 11번 다녀온다면 약 2200이겠으나 넉넉하게 3000으로
    company = (t[0], t[1]) # 회사의 위치
    home = (t[2], t[3]) # 집의 위치
    client = []
    for i in range(n):
        client.append((t[i*2+4], t[i*2+5])) # 고객들의 위치

    dfs(list(range(n)), 0, 0)

    print('#'+str(test+1)+' '+str(minDist))