def solution(new_id):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_big = alphabet.upper()
    spec = '-_.'
    
    temp_answer = ''
    for s in new_id:
        if s in alphabet_big:
            temp_answer += s.lower()
        else:
            temp_answer += s
    new_id = temp_answer
    
    temp_answer = ''
    for s in new_id:
        if s in alphabet or s in spec or s.isnumeric():
            temp_answer += s
    new_id = temp_answer
    
    temp_answer = ''
    for i in range(len(new_id)):
        if i == 0:
            temp_answer += new_id[i]
        else:
            if new_id[i] == '.':
                if new_id[i-1] == '.':
                    continue
                else:
                    temp_answer += new_id[i]
            else:
                temp_answer += new_id[i]
    new_id = temp_answer
    
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if new_id == '':
        new_id = 'a'
    
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:len(new_id)-1]
    
    while len(new_id) < 3:
        new_id += new_id[-1]
                    
    answer = new_id   
    return answer