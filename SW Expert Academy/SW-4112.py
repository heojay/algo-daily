# SW Expert Academy
# 4112. 이상한 피라미드 탐험
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWJHmLraeEwDFAUH&categoryId=AWJHmLraeEwDFAUH&categoryType=CODE&&&

'''
층과 순서에 따라 새로운 좌표 체계를 만듬.
1은 (0,0), 2는 (1,0) 3은 (1,1)...
이동 가능한 방향은 총 6가지로
(1,1), (1,0), (0,1), (-1,0), (0,-1), (-1,-1)
따라서, 두 점의 좌표 차이 x축 y축의 부호가 같으면 (1,1) 혹은 (-1,-1)로 움직일 수 있기 때문에 두 차이 중 큰 값이
반대면 정직하게 두 방향 모두 따로 움직여줘야 하기 때문에 두 차이의 합이 답이 된다.
'''


def coord(n): # 새로운 좌표체계로
    s = 0
    while True:
        if(s*(s+1)//2 < n and n <= (s+2)*(s+1)//2):
            return s, n-1-s*(s+1)//2
        s += 1

for test in range(int(input())):
    a, b = map(int, input().split())

    a1, a2 = coord(a)
    b1, b2 = coord(b)

    if ((a1 - b1) * (a2 - b2) < 0): # 부호가 다르다
        ans = abs(a1 - b1) + abs(a2 - b2)
    else: # 부호가 같다
        ans = max(abs(a1 - b1), abs(a2 - b2))

    print('#' + str(test+1) + ' ' + str(ans))