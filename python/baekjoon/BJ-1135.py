# Baekjoon Online Judge
# 1135. 뉴스 전하기
# https://www.acmicpc.net/problem/1135

'''
이 문제는 동시에 전화를 걸 수 없음에서 문제가 발생한다.
따라서 모두 전화를 돌리기까지 오래 걸리는 사람을 우선적으로 전화하고, 그에 따라 발생하는 비용을 계산한다.
'''

N = int(input())
emp = list(map(int, input().split()))
son = {}

for i in range(N):
    son[i] = []

for i, x in enumerate(emp):
    if i == 0:
        continue
    son[x].append(i)

def time_sons(x):
    if son[x]:
        times = [time_sons(s) for s in son[x]]
        times.sort(reverse=True)
        return max(t + i + 1 for i, t in enumerate(times))
    else:
        return 0

print(time_sons(0))