# SW Expert Academy
# 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD&categoryId=AV14eWb6AAkCFAYD&categoryType=CODE

'''
전세계 알고리즘 교과서에 있을만한 예제 문제.

'''
def valid(a, b):
    if(a+b in ['()', '[]', '{}', '<>']):
        return True
    else:
        return False

for test in range(10):
    l = int(input())
    k = input()
    x = []
    for i in range(l):
        if(len(x) == 0):
            x.append(k[i])
        elif k[i] in ['(', '[', '{', '<']:
            x.append(k[i])
        else:
            if(valid(x[-1], k[i])):
                x.pop()
            else:
                break
    ans = int(not bool(len(x)))

    print("#" + str(test+1) + " " + str(ans))