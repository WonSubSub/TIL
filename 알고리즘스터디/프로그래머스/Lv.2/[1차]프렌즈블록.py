def solution(m, n, matrix):
    answer = 0
    temp_answer = -1
    temp_matrix = []
    for i in range(len(matrix)):
        matrix[i] = list(map(str, matrix[i]))
    
    while temp_answer != answer:
        temp_answer = answer
        for x in range(m-1):
            for y in range(n-1):
                eraser = [matrix[x][y].upper(), matrix[x][y+1].upper(), matrix[x+1][y].upper(), matrix[x+1][y+1].upper()]
                if len(set(eraser)) == 1:
                    matrix[x][y] = matrix[x][y].lower()
                    matrix[x][y+1] = matrix[x][y+1].lower()
                    matrix[x+1][y] = matrix[x+1][y].lower()
                    matrix[x+1][y+1] = matrix[x+1][y+1].lower()

        for x in range(m):
            for y in range(n):
                if matrix[x][y] != matrix[x][y].upper():
                    matrix[x][y] = '0'
                    answer += 1
        
        for i in range(30):
            for x in range(1, m):
                for y in range(n):
                    if matrix[x][y] == '0':
                        matrix[x][y] = matrix[x-1][y]
                        matrix[x-1][y] = '0'
            
    return answer