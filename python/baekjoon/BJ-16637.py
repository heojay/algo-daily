# Baekjoon Online Judge
# 16637. 괄호추가하기
# https://www.acmicpc.net/problem/16637

'''
이렇게 푸는게 아닐 것 같은데!!! 라는 생각을 한참 하면서 푼 문제.
N이 1일때를 생각 안했다.
나중에 질문게시판보니까 DP로 푸는 방법이 있었겠구나 싶었다.
eval이 생각 안나서 새로 만들기도 하고.
사소한것도 참고하지 않고 푸는 것에 의의를 두기로...
'''

N = int(input())
s = input()
digit = list(map(int, [s[i] for i in range(0, N, 2)]))
symbol = [s[i] for i in range(1, N, 2)]

def cal(a, b, c):
    if(b == '*'):
        return a*c
    if(b == '+'):
        return a+c
    if(b == '-'):
        return a-c

T = -99999999999

if(N == 1):
    T = digit[0]
    count = 0
else:
    count = 2**(N//2-1)

for i in range(count):
    newdigit = []
    newsymbol = []
    flag = True
    x = ((N//2) - len(bin(i)[2:])) *'0' + bin(i)[2:]

    for j in range(N//2-1):
        if(x[j] == '1' and x[j+1] == '1'):
            flag = False
    if(not flag):
        continue

    dc = 0
    
    for j in range(N//2):
        if(x[j] == '0'):
            if(dc <= j):
                newdigit.append(digit[dc])
                dc += 1
            newsymbol.append(symbol[j])
        else:
            newdigit.append(cal(digit[dc],symbol[j], digit[dc+1]))
            dc += 2

    while dc < N//2 + 1:
        newdigit.append(digit[dc])
        dc += 1
    
    ans = newdigit[0]
    for i in range(len(newsymbol)):
        ans = cal(ans, newsymbol[i], newdigit[i+1])
    T = max(ans, T)

print(T)
