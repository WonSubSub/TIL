def solution(n):
    bin_n = str(bin(n))[2:]
    on_cnt = 0
    edge = -1
    edge_num = ''
    left_num = ''
    for i in range(len(bin_n)-1,-1,-1):
        if bin_n[i] == '0':
            if on_cnt > 0:
                edge_num = bin_n[i+1:]
                left_num = bin_n[:i]
                break
        else:
            on_cnt += 1
    if left_num == '':
        edge_num = bin_n
    one_cnt = edge_num.count('1')
    num = ''
    for i in range(len(edge_num)):
        if i < one_cnt-1:
            num += '1'
        else:
            num += '0'
    num += '1'
    num = num + left_num[::-1]

    ans = 0
    for i in range(len(num)):
        if num[i] == '1':
            ans += int(num[i]) * (2**i)
    
    return ans