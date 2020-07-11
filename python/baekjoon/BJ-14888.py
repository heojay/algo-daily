# Baekjoon Online Judge
# 14888. 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

'''
간단한 DFS 문제.
'''

N = int(input())
nums = list(map(int, input().split()))
nums.append(0) # the end
plus, mins, mult, divd = map(int, input().split())

ans = [-2e9, 2e9]

def dfs(total, ind, plus, mins, mult, divd):
    now = nums[ind]
    if now == 0:
        ans[0] = max(ans[0], total)
        ans[1] = min(ans[1], total)
        return
    if plus != 0:
        dfs(total+now, ind+1, plus-1, mins, mult, divd)
    if mins != 0:
        dfs(total-now, ind+1, plus, mins-1, mult, divd)
    if mult != 0:
        dfs(total*now, ind+1, plus, mins, mult-1, divd)
    if divd != 0:
        if total < 0:
            result = total * -1 // now * -1
        else:
            result = total // now
        dfs(result, ind+1, plus, mins, mult, divd-1)

dfs(nums[0], 1, plus, mins, mult, divd)

print(ans[0], ans[1],sep='\n')