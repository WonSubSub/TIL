number = list(map(int, input().split(' ')))

ans = 0

temp1 = [number[0], number[1], number[2], number[3]]
temp2 = [number[1], number[2], number[3], number[0]]
temp3 = [number[2], number[3], number[0], number[1]]
temp4 = [number[3], number[0], number[1], number[2]]
clock_number = min(temp1, temp2, temp3, temp4)

def check_clock(number):
    clock = 0
    a = number // 1000
    b = (number // 100) % 10
    c = (number // 10) % 10
    d = number % 10
    numbers = [a, b, c, d]
    temp1 = [numbers[0], numbers[1], numbers[2], numbers[3]]
    temp2 = [numbers[1], numbers[2], numbers[3], numbers[0]]
    temp3 = [numbers[2], numbers[3], numbers[0], numbers[1]]
    temp4 = [numbers[3], numbers[0], numbers[1], numbers[2]]
    clock_number = min(temp1, temp2, temp3, temp4)
    if numbers == clock_number:
        clock = 1
    return clock
        

for i in range(1111, clock_number[0]*1000 + clock_number[1]*100 + clock_number[2]*10 + clock_number[3] + 1):
    if check_clock(i):
        ans += 1

print(ans)