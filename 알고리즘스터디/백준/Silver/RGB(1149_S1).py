n = int(input())

matrix = []
red = 0
green = 0
blue = 0
for i in range(n):
    numbers = list(map(int, input().split()))
    if i == 0:
        red += numbers[0]
        green += numbers[1]
        blue += numbers[2]
        matrix.append([red, green, blue])
    else:
        red = numbers[0] + min(matrix[i-1][1], matrix[i-1][2])
        green = numbers[1] + min(matrix[i-1][0], matrix[i-1][2])
        blue = numbers[2] + min(matrix[i-1][1], matrix[i-1][0])
        matrix.append([red, green, blue])

print(min(matrix[-1][0], matrix[-1][1], matrix[-1][2]))