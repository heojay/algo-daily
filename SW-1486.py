# SW Expert Academy
# 1486. 장훈이의 높은 선반
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw&categoryId=AV2b7Yf6ABcBBASw&categoryType=CODE

'''
모든 경우를 다 따질법 하다. N이 20밖에 안되서..
다만 중복만 방지해줄 것.

처음에는 그냥 매번 P에 내가 구한 값이 있나 없나 확인해줬다가 특정 TC를 통과 못해서
try-except를 통해 중복을 확인해줬다.
가장 큰 답이 20만이니까, 20만짜리 배열을 만들어서 이미 나온 값인지 확인해도 괜찮지 않을까.

...
사실 마음에는 안든다.
'''


for test in range(int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    P = {}

    for i in range(N):
        cand = [] # 추가될 수 있는 후보, 바로 append하면 힘들다.
        for total_height in P.keys():
            try:
                P[total_height + H[i]] += 1 # 이미 있는 값이면 통과한다. 없으면 새로 만들어야.
            except:
                cand.append(total_height + H[i])

        if(H[i] not in P):
            cand.append(H[i]) # 자기 자신에서 시작하는 합. 엄밀히 말하면 이것도 try-except로 해결해줬어야 했다.

        for height in cand:
            P[height] = 1
    
    ans = 200000

    for total_height in P:
        if(total_height >= B and total_height - B < ans): # 더 크면서, 가장 차이가 작은 것.
            ans = total_height - B
    
    print("#"+str(test+1)+" "+str(ans))