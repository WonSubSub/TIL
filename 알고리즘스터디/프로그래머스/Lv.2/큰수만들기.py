from collections import deque

def solution(number, k):

    number = deque(map(int, number))
    ans_q = deque()
    ans_q.append(number.popleft())
    while number:
        while len(ans_q) > 0 and number[0] > ans_q[-1] and k > 0:
            ans_q.pop()
            k -= 1
        ans_q.append(number.popleft())
    if k > 0:
        while k != 0:
            ans_q.pop()
            k -= 1
    answer = ''.join(map(str, ans_q))
    return answer
