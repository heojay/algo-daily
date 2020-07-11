'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

# 가장 간단한 방법 : Merge Sort처럼 하나씩 하기 O((n+m))
# O(log(m+n)) 풀이

def findMedianSortedArrays(A, B) -> float:
    lenA = len(A)
    lenB = len(B)
    
    if lenA > lenB:
        A, B = B[:], A[:]
        lenA, lenB = lenB, lenA
    
    halfLen = (lenA + lenB + 1) // 2

    minA = 0
    maxA = lenA

    # A랑 B의 일부를 합쳐서 앞쪽 반을 만들어보자. 경계를 어디로 잡아야 할까?
    # posA + posB가 전체 배열의 절반이면서,
    # 한 배열의 값이 다른 배열의 값보다 크지만 그 다음 값보다는 작은 위치.

    while minA <= maxA:
        posA = minA + (maxA - minA) // 2
        posB = halfLen - posA

        x = A[posA - 1] if posA > 0 else None
        nx = A[posA] if posA < lenA else None
        
        y = B[posB - 1] if posB > 0 else None
        ny = B[posB] if posB < lenB else None

        if x and ny and x > ny:
            maxA = posA - 1
        elif y and nx and y > nx:
            minA = posA + 1
        else:
            if x == None: # 한 배열만으로 만든 경우
                ans = y
            elif y == None:
                ans = x
            else:
                ans = max(x, y)
        
            if (lenA + lenB) % 2:
                return ans
            else:
                if nx == None:
                    ans += ny
                elif ny == None:
                    ans += nx
                else:
                    ans += min(nx, ny)
                return ans / 2