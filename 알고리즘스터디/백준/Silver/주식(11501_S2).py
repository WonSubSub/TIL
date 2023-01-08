import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    answer = 0
    days = int(input())
    prices = list(map(int, input().split()))
    
    max_price = prices[-1]
    for i in range(days-2, -1, -1):
        if prices[i] <= max_price:
            answer += max_price - prices[i]
        else:
            max_price = prices[i]
    print(answer)
