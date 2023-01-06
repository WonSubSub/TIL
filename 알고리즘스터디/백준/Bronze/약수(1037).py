n = int(input())
divisors = list(map(int, input().split(' ')))

print(sorted(divisors)[0] * sorted(divisors)[-1])