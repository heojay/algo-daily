'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

가장 간단한 풀이는 앞에서부터 모든 subarray를 조사하는 것이겠지만, O(N^2)의 시간 복잡도를 가진다.
따라서 0과 1의 누적 갯수 차이가 같은 두 지점을 조사하는 방식을 이용하자.

'''

def findMaxLength(nums):
    s = 0

    until = {0:[-1,-1]}

    for i,x in enumerate(nums):
        if x == 0:
            s += 1
        else:
            s -= 1

        if until.get(s):
            until[s][1] = i
        else:
            until[s] = [i, None]

    ans = 0

    print(until)

    for v in until.values():
        if v[1] != None:
            ans = max(ans, v[1] - v[0])

    return ans

findMaxLength([1,1,1,1,0,0,0,1,0,0,1,0,0,1])