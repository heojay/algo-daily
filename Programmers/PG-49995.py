# Programmers Coding Test
# 49995. 쿠키 구입
# https://programmers.co.kr/learn/courses/30/lessons/49995

'''
연속된 쿠키를 가지고 비교하면 되는 것.
시점을 하나씩 움직이면서 왼쪽 오른쪽 합에 따라서 쿠키합의 크기를 점점 늘려가면 된다.
한 개씩으로 시작해서, 왼쪽이 더 크면 오른쪽을 하나 더 늘리고, 오른쪽이 더 크면 오른쪽의 하나를 왼쪽에게 주는 식.
그 과정에서 양쪽이 같으면 갱신. N^2이지만 쿠키가 어차피 2000개라 상관 없다.
'''


def solution(cookie):
    answer = 0
    length = len(cookie)
    
    for l in range(length-1):
        left = cookie[l]
        m = l
        right = cookie[m+1]
        r = m+1
        if(left == right):
            answer = max(left, answer)
        
        while True:
            if(left <= right):
                if(left == right):
                    answer = max(left, answer)
                m += 1
                if(m >= length):
                    break
                left += cookie[m]
                right -= cookie[m]
                
            elif(left > right):
                r += 1
                if(r >= length):
                    break
                right += cookie[r]
                
    return answer