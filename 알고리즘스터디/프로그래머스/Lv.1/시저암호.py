def solution(s, n):
    answer = ''
    alphabet_small = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_big = alphabet_small.upper()
    
    alphabet_small = list(map(str, alphabet_small))
    alphabet_big = list(map(str, alphabet_big))
    for alphabet in s:
        if alphabet in alphabet_small:
            if alphabet_small.index(alphabet) + n >= len(alphabet_small):
                answer += alphabet_small[alphabet_small.index(alphabet) + n - len(alphabet_small)]
            else:
                answer += alphabet_small[alphabet_small.index(alphabet) + n]
        elif alphabet in alphabet_big:
            if alphabet_big.index(alphabet) + n >= len(alphabet_big):
                answer += alphabet_big[alphabet_big.index(alphabet) + n - len(alphabet_big)]
            else:
                answer += alphabet_big[alphabet_big.index(alphabet) + n]
        else:
            answer += alphabet
                
    return answer