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