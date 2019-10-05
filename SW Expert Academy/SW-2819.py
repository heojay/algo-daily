# SW Expert Academy
# 2819. 격자판의 숫자 이어 붙이기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&&&

'''
시작 지점이 16개고, 4방향의 6번 이동이라
총 방법 수는 16 * 4^6 = 2^16 이라서
다 해보면 됨.
'''
dir = [(0,1),(1,0),(0,-1),(-1,0)] # 4방향
ans = []

def valid(x,y): # 해당 위치가 격자 안에 존재하는가.
    return x >= 0 and x < 4 and y >= 0 and y < 4

def dfs(now, head): # 현재 숫자열, 가장 최근에 방문한 위치
    if len(now) == 7: # 7자리수면 배열에 포함하고 return
        ans.append(now)
        return
    else: # 아니면 4방향에 해당하는 값을 넣어준다.
        x, y = head
        for i in range(4):
            dirx, diry = dir[i]
            if(valid(x+dirx, y+diry)):
                head = (x+dirx, y+diry)
                now += str(MAP[x+dirx][y+diry])
                dfs(now, head)
                now = now[:-1]

for test in range(int(input())):
    MAP = [list(map(int, input().split())) for _ in range(4)]

    ans = []
    for x in range(4):
        for y in range(4):
            dfs(str(MAP[x][y]),(x,y))
    ans = set(ans)
    print('#' + str(test+1) + ' ' + str(len(ans)))