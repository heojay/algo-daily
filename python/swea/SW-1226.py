# SW Expert Academy
# 1226. [S/W 문제해결 기본] 7일차 - 미로1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE

'''
DFS를 깔끔하게 구현하는 것을 연습 중.
평범한 미로찾기 문제다.
'''
MAP_SIZE = 16

def valid(x, y, MAP, VISIT):
    if(x < 0 or y < 0 or x >= MAP_SIZE or y >= MAP_SIZE or MAP[x][y] == 1 or VISIT[x][y]):
        return False
    else:
        return True

def DFS(x, y, MAP, VISIT, endx, endy):
    if(x == endx and y == endy):
        return
    else:
        for dir in [(0,1), (1,0), (0,-1), (-1,0)]:
            if(valid(x+dir[0], y+dir[1], MAP, VISIT)):
                VISIT[x+dir[0]][y+dir[1]] = 1
                if(x+dir[0] == endx and y+dir[1] == endy):
                    return
                DFS(x+dir[0], y+dir[1], MAP, VISIT, endx, endy)
                VISIT[x+dir[0]][y+dir[1]] = 0

for _ in range(10):
    ans = [0]
    test = input()
    MAP = [list(map(int, list(input()))) for __ in range(MAP_SIZE)]
    VISIT = [[0 for i in range(MAP_SIZE)] for j in range(MAP_SIZE)]

    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if(MAP[i][j] == 2):
                x,y = i,j
            if(MAP[i][j] == 3):
                endx, endy = i, j
    VISIT[x][y] = 1
    DFS(x,y, MAP, VISIT, endx, endy)

    print("#" + test + " " + str(VISIT[endx][endy]))