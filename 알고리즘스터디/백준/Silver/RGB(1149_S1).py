n = int(input())

matrix = []
for i in range(n):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

[[9,1,11],
 [280,280,291],
 [100,1,100],
 [200,1,200],
 [800,1,800],
 [650,1,650]]
[26, 49, 13]
[40, 60, 89]
[83, 57, 99]

answer = 0
for i in range(len(matrix)):
    if i == 0:

71
39
44

32 39
83 44
55 39

51 55 39
37 32 39
63 32 39

89 37 32 39
29 63 32 39
100 37 32 39
dp