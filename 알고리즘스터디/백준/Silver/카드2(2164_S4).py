import sys
input = sys.stdin.readline
n = int(input())

# from collections import deque
# numbers = deque()
# for i in range(1, n+1):
#     numbers.append(i)

# while len(numbers) > 2:
#     numbers.popleft()
#     numbers.append(numbers.popleft())

# print(numbers[-1])

numbers = []
if n % 2 == 0:
    for i in range(1, int(n/2) + 1):
        numbers.append(i * 2)
else:
    numbers.append(n)
    for i in range(1, int(n/2) + 1):
        numbers.append(i * 2)

def change(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        if len(numbers) % 2 == 0:
            new_numbers = []
            for i in range(1, len(numbers), 2):
                new_numbers.append(numbers[i])
            return change(new_numbers)
        else:
            new_numbers = []
            new_numbers.append(numbers[-1])
            for i in range(1, len(numbers), 2):
                new_numbers.append(numbers[i])
            return change(new_numbers)

answer = change(numbers)
print(answer)