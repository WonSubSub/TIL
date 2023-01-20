def solution(fees, records):
    answer = []
    
    inout = {}
    pay = {}
    for i in range(len(records)):
        r = records[i].split()
        if r[2] == 'IN':
            inout[r[1]] = 1
        else:
            inout[r[1]] = 0
        pay[r[1]] = 0
        records[i] = r
    
    temp = 0
    for i in range(len(records)-1, -1, -1):
        h, m = map(int, records[i][0].split(':'))
        time = h*60 + m
        if records[i][-1] == "IN":
            if inout[records[i][1]] == 1:
                pay[records[i][1]] += 23*60 + 59 - time
                inout[records[i][1]] = 0
            else:
                pay[records[i][1]] -= time
        else:
            pay[records[i][1]] += time
    
    pay_list = []
    for i in pay.keys():
        pay_list.append([i, int(pay[i])])
    pay_list.sort()
    
    for car, times in pay_list:
        temp = 0
        if times >= fees[0]:
            times -= fees[0]
            temp += fees[1]
            if times%fees[2] == 0:
                temp += (times//fees[2]) * fees[3]
            else:
                temp += (times//fees[2] + 1) * fees[3]
        else:
            temp += fees[1]
        answer.append(temp)

    return answer