from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights = deque(truck_weights)
    q = deque([0]*bridge_length)
    total = 0
    
    while q:
        answer += 1
        total -= q.popleft()
        if truck_weights:
            if truck_weights[0] + total <= weight:
                truck = truck_weights.popleft()
                total += truck
                q.append(truck)
            else:
                q.append(0)

    return answer