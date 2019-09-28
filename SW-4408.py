# SW Expert Academy
# 4408. 자기 방으로 돌아가기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWFPoj1qANoDFAV0&categoryId=AWFPoj1qANoDFAV0&categoryType=CODE


'''
1. 이동경로를 파악해서 겹치는 구간을 알아낸다.
2. 정답은 가장 많이 겹치는 만큼 + 1
이유는 간단한데, 어차피 겹치는 구간은 단위 시간동안 한 번씩 빠지게 된다.
안 빠지는 경우가 없다. 적어도 한 명의 누군가는 그 경로로 움직일 것이기 때문

'''

for test in range(int(input())):
    n = int(input())
    route = [0] * 200
    for i in range(n):
        x, y = map(int, input().split()) # 시작점과 끝점
        if (x > y):
            x, y = y, x # 시작점이 끝점보다 큰 경우를 고려한다.
        for i in range((x-1)//2, (y+1)//2):
            route[i] += 1

    print('#'+str(test+1)+' '+str(max(route)))