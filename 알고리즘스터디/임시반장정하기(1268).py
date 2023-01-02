n = int(input())

matrix = []
student_count = [0] * n

def count(matrix, index, student_count):
    for i in range(index):
        for a in range(5):
            if matrix[i][a] == matrix[index][a]:
                student_count[i] += 1
                student_count[index] += 1
                break
    
for i in range(n):
    bans = list(map(int, input().split(' ')))
    matrix.append(bans)
    if i != 0:
        count(matrix, i, student_count)
    # print(student_count)

print(student_count.index(max(student_count)) + 1)