# SW Expert Academy
# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE

'''
크게 어려운 문제는 아니다. 뒤에서 올라가면서 확인해주면 되는 문제.
별개로 오늘 네이버 해커톤 코딩테스트가 있었는데 생각보다 난이도가 쉬웠다.
학부생에게 기대하는 바가 적다는건가.
'''


for __ in range(10):
    test = int(input())
    MAP = [input().split() for _ in range(100)]

    for i in range(100):
        if(MAP[99][i] == '2'):
            s = [99, i]
            break
    
    while s[0] != 0:
        
        if s[1] != 0 and MAP[s[0]][s[1]-1] == '1':
            while (s[1] != 0 and MAP[s[0]][s[1]-1] == '1'):
                s[1] -= 1
            s[0] -= 1
            continue

        if s[1] != 99 and MAP[s[0]][s[1]+1] == '1':
            while (s[1] != 99 and MAP[s[0]][s[1]+1] == '1'):
                s[1] += 1
            s[0] -= 1
            continue

        s[0] -= 1

    print("#" + str(test) + " " + str(s[1]))