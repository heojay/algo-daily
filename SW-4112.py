# SW Expert Academy
# 4112. 이상한 피라미드 탐험
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWJHmLraeEwDFAUH&categoryId=AWJHmLraeEwDFAUH&categoryType=CODE&&&


def coord(n):
    s = 0
    while True:
        if(s*(s+1)//2 < n and n <= (s+2)*(s+1)//2):
            return s, n-1-s*(s+1)//2
        s += 1

for test in range(int(input())):
    a, b = map(int, input().split())

    a1, a2 = coord(a)
    b1, b2 = coord(b)

    if ((a1 - b1) * (a2 - b2) < 0):
        ans = abs(a1 - b1) + abs(a2 - b2)
    else:
        ans = max(abs(a1 - b1), abs(a2 - b2))

    print('#' + str(test+1) + ' ' + str(ans))