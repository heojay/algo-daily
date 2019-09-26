# SW Expert Academy
# 3752. 가능한 시험 점수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn&categoryId=AWHPkqBqAEsDFAUn&categoryType=CODE

#가능한 최대 점수는 몇 점인가 = 100 * 100



for test in range(int(input())):
    N = int(input())
    points = list(map(int, input().split()))

    seen = [0] * 10001 # 이미 추가한 총점은 무시할 수 있도록
    totals = [0]
    seen[0] = 1 # 0점은 있으니까

    for point in points:
        cands = []
        for total in totals:
            cands.append(total+point) #기존에 가능했던 값에 새로운 점수를 추가하자.
        for cand in cands:
            if(seen[cand]):
                continue
            else:
                seen[cand] = 1
                totals.append(cand)

    print("#" + str(test+1) + " " + str(len(totals)))