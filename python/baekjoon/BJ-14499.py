# Baekjoon Online Judge
# 14499. 주사위 굴리기
# https://www.acmicpc.net/problem/14499

'''
어려울 것 없는 구현 문제.
머리 속에서 주사위를 굴리기만 하면 된다.
문제를 잘못 읽어서 조금 시간이 걸리긴 했지만, 구현 자체는 금방 끝냄.
'''

def roll(dice, dir, badak):
    if(dir == 1):
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]    
    elif(dir == 2):
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif(dir == 3):
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
    elif(dir == 4):
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]
    
    if(badak == 0):
        badak = dice[5]
    else:
        dice[5] = badak
        badak = 0
    return dice, badak


N, M, x, y, K = map(int, input().split())
MAP = []
MOVE = {1 : (0, 1), 2: (0, -1), 3 : (-1, 0), 4 : (1, 0)}
DICE = [0]*6

for _ in range(N):
    MAP.append(list(map(int, input().split())))
for dir in list(map(int, input().split())):
    nx = MOVE[dir][0] + x
    ny = MOVE[dir][1] + y

    if(nx not in range(N) or ny not in range(M)):
        continue
    x = nx
    y = ny
    DICE, MAP[x][y] = roll(DICE, dir, MAP[x][y])
    print(DICE[0])