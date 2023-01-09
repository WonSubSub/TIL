def solution(N, stages):
    answer = []
    success = []
    fail = []
    rate = []
    
    for i in range(N+1):
        success.append([i,0])
        fail.append([i,0])
        rate.append([0,i])
        
    for i in range(1, N+1):
        fail[i][1] += stages.count(i)
        
    for stage in stages:
        if stage > N:
            for i in range(len(success)):
                success[i][1] += 1
        else:
            for i in range(1,stage+1):
                success[i][1] += 1
    
    for i in range(1,N+1):
        if success[i][1] != 0:
            rate[i][0] += fail[i][1] / success[i][1]
    rate.remove([0,0])
    rate.sort(key=lambda x : (-x[0], x[1]))
    # print(fail)
    # print(success)
    # print(rate)
    for i in range(N):
        answer.append(rate[i][1])
        
    return answer