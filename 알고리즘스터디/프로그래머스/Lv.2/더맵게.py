import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    while scoville[0]<K:
        try:
            heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        except:
            return -1
        count+=1

    return count

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
    if scoville[0] < K:
        answer = -1
    return answer