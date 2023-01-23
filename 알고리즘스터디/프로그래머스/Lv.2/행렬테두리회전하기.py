from collections import deque
def solution(rows, columns, queries):
    answer = []
    
    q = deque()
    matrix = [[(columns*y+x+1) for x in range(columns)] for y in range(rows)] 
    def change(query, matrix):
        q_num = deque()
        q_cordinate = deque()
        a, b, c, d = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        for y in range(b, d+1):
            q_num.append(matrix[a][y])
            q_cordinate.append([a,y])
        for x in range(a+1, c+1):
            q_num.append(matrix[x][d])
            q_cordinate.append([x,d])
        for y in range(d-1, b-1, -1):
            q_num.append(matrix[c][y])
            q_cordinate.append([c,y])
        for x in range(c-1, a,-1):
            q_num.append(matrix[x][b])
            q_cordinate.append([x,b])
        q_num.appendleft(q_num.pop())
        for i in range(len(q_cordinate)):
            x, y = q_cordinate[i][0], q_cordinate[i][1]
            matrix[x][y] = q_num[i]
        return min(q_num)
                
    for query in queries:
        answer.append(change(query, matrix))
    
    return answer