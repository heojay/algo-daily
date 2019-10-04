# SW Expert Academy
# 1249. [S/W 문제해결 응용] 4일차 - 보급로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE

# 재밌는게, '복구작업에 드는 시간이 작다 != 실제 최단거리다' 라는 것.
# 즉, 아무리 뺑뺑 돌아가도 복구작업이 최소인 경로가 있을 수 있다는 것이다.
# 탐색의 횟수를 줄이기 위해서는 어떻게 해야 할까.
# 매번 최소로 업데이트 될 때마다, 해당하는 위치의 주변 4방향만을 재탐색하자.


for test in range(int(input())):
    n = int(input())
    MAP = [list(map(int,list(input()))) for _ in range(n)]
    costs = [[100000 for _ in range(n)] for __ in range(n)]
    costs[0][0] = 0

    check = [(0,0)]

    # 이하에서는 방향마다 체크해준다. for문 2개로 구현할 수도 있지만 복붙이 더 편하니까..

    while check:
        x, y = check.pop()
        if(x != 0):
            if(costs[x][y] + MAP[x][y] < costs[x-1][y]):
                costs[x-1][y] = costs[x][y] + MAP[x][y]
                check.append((x-1, y))
        if(x != n-1):
            if(costs[x][y] + MAP[x][y] < costs[x+1][y]):
                costs[x+1][y] = costs[x][y] + MAP[x][y]
                check.append((x+1, y))
        if(y != 0):
            if(costs[x][y] + MAP[x][y] < costs[x][y-1]):
                costs[x][y-1] = costs[x][y] + MAP[x][y]
                check.append((x, y-1))
        if(y != n-1):
            if(costs[x][y] + MAP[x][y] < costs[x][y+1]):
                costs[x][y+1] = costs[x][y] + MAP[x][y]
                check.append((x, y+1))

    ans = costs[n-1][n-1]
    
    print("#"+str(test+1)+" "+str(ans))