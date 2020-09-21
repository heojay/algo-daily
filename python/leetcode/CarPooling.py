'''
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

'''

# 오랜만에 PS가 하고 싶었다.
# start, end location의 passanger 합을 위치별로 dict로 관리해서 풀기로 했다.
# 이 경우에 사실, 들리지 않은 곳을 조회한다는 단점이 있지만, 어차피 location 값이 1000 이내라.
# 만약 그 부분이 신경쓰인다면, 그냥 start, end를 가지고 정렬하는 편이 나을 것.

from collections import defaultdict

def carPooling(trips: List[List[int]], capacity: int) -> bool:
    finishedPos = 0

    startLocations = defaultdict(int)
    endLocations = defaultdict(int)

    for trip in trips:
        c, s, e = trip
        startLocations[s] += c
        endLocations[e] += c
        if e > finishedPos:
            finishedPos = e
    
    currentCapacity = 0
    for i in range(finishedPos+1):
        currentCapacity += startLocations[i] - endLocations[i]
        if currentCapacity > capacity:
            return false

    return true