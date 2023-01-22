def solution(arr):
    answer = []

    ones = 0
    zeros = 0
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][y] == 1:
                ones += 1
            else:
                zeros += 1
    def check(arr, x, y, n, ones, zeros):
        check_list = set()
        for a in range(x, x+n):
            for b in range(y, y+n):
                check_list.add(arr[a][b])
                if len(check_list) == 2:
                    break
            if len(check_list) == 2:
                break
        if len(check_list) == 1:
            if 1 in check_list:
                ones -= 3
            else:
                zeros -= 3
        return ones, zeros
    
    n = 2
    while len(arr)//n != 0:
        for i in range(len(arr)//n):
            for k in range(len(arr)//n):
                x = i*n
                y = k*n
                ones, zeros = check(arr,x,y,n,ones,zeros)
        n = n * 2
    answer = [zeros,ones]
    return answer