from collections import deque

n = int(input())
for i in range(n):
    m, n, x, y = map(int, input().split())
    if m > n:
        m, n, x, y = n, m, y, x
    # m_q = deque(x for x in range(1, m+1))
    # n_q = deque(x for x in range(1, n+1))
    m_q = [x for x in range(1, m+1)]
    n_q = [x for x in range(1, n+1)]
    cnt = 0 
    
    if y == x:
        print(x)
    elif y > x:
        sub = y-x
    