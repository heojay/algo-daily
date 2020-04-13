'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

'''

#1. 단순하게 문제를 그대로 이행하는 풀이

def lastStoneWeight1(stones):
    while len(stones) > 1:
        y = max(stones)
        stones.remove(y)
        x = max(stones)
        stones.remove(x)
        if y - x > 0:
            stones.append(y-x)

    if stones:
        return stones[0]
    else:
        return 0


#2. 1번의 경우 remove가 항상 O(N) 만큼 걸림. heapq로 이 과정을 O(logN)으로 줄여보자.

import heapq

def lastStoneWeight2(stones):
    heapstone = [-x for x in stones] # minheap 이기 때문에
    heapq.heapify(heapstone)
    while len(heapstone) > 1:
        y = heapq.heappop(heapstone)
        x = heapq.heappop(heapstone)
        if y != x:
            heapq.heappush(heapstone, y-x)
    
    if heapstone:
        return -heapq.heappop(heapstone)
    else:
        return 0