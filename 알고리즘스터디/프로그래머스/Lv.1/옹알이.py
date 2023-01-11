def solution(babbling):
    answer = 0
    "aya", "ye", "woo", "ma"
    
    for s in babbling:
        s = s.replace('aya', '1')
        s = s.replace('ye', '2')
        s = s.replace('woo', '3')
        s = s.replace('ma', '4')
        if s.isnumeric():
            s = list(map(int, s))
            ist = True
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    ist = False
            if ist:
                answer += 1
        
    return answer