# SW Expert Academy
# 1238. [S/W 문제해결 기본] 10일차 - Contact
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD&categoryId=AV15B1cKAKwCFAYD&categoryType=CODE

'''
요즘 바빠서 머리가 잘 안돌아가기도 하고
오랜만에 그냥 그래프 문제가 풀어보고 싶었음..
input 형식이 이상하네.
'''

test = 1

try:
    while test:
        n, start = map(int, input().split())
        x = list(map(int, input().split()))
        MAP = {i : [] for i in range(101)}
        for i in range(n//2):
            MAP[x[i*2]].append(x[i*2+1])
        for key in MAP.keys():
            MAP[key] = list(set(MAP[key])) # 내가 연락해야 할 사람들

        seen = [0] * 101
        contact = []
        next_contact = [start]
        
        while next_contact: # 더 연락할 사람이 없다면
            contact, next_contact = next_contact[:], []
            for s in contact:
                if(seen[s]):
                    continue
                seen[s] = 1
                for e in MAP[s]:
                    if(not seen[e]):
                        next_contact.append(e)

        print("#" + str(test) + " " + str(max(contact)))
        test += 1
except:
    pass