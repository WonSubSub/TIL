def solution(today, terms, privacies):
    answer = []
    todayy = int(today.split('.')[0])
    todaym = int(today.split('.')[1])
    todayd = int(today.split('.')[2])
    today_days = todayy * 12 * 28 + todaym * 28 + todayd
    
    for s in terms:
        name, month = s.split()
        month = int(month)
        for i in range(len(privacies)):
            if privacies[i][-1] == name:
                date = privacies[i].split()[0]
                datey = int(date.split('.')[0])
                datem = int(date.split('.')[1])
                dated = int(date.split('.')[2])

                datey += month // 12
                datem += month % 12
                
                days = datey * 12 * 28 + datem * 28 + dated
                if days <= today_days:
                    answer.append(i+1)
        
    answer.sort()
    
    return answer