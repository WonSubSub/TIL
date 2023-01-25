from collections import deque
def solution(name):   
    if len(set(map(str, name))) == 1 and 'A' in name:
        answer = 0
    else:
        answer = 0
        alphabet = 'opqrstuvwxyzabcdefghijklmn'
        alphabet = alphabet.upper()

        a_ind = alphabet.index('A')
        alphabet_list = []
        for s in name:
            ind = alphabet.index(s)
            alphabet_list.append(abs(a_ind - ind))

        alphabet_list = deque(alphabet_list)

        index_list = []
        for num in alphabet_list:
            if num == 0:
                index_list.append(num)
            else:
                index_list.append(1)

        cnt_list = []
        for i in range(len(index_list)-1):
            if index_list[i] == 1:
                a = i*2
                new = index_list[i+1:]
                if 1 in new:
                    new_ind = new.index(1)
                    b = len(new) - new_ind
                    cnt_list.append(a+b)
                else:
                    cnt_list.append(i)
        cnt_list.append(len(index_list)-index_list.index(1))
        newnewnew = index_list[::-1]
        newnewnew.insert(0, newnewnew.pop())
        for i in range(len(newnewnew)-1):
            if newnewnew[i] == 1:
                a = i*2
                new = newnewnew[i+1:]
                if 1 in new:
                    new_ind = new.index(1)
                    b = len(new) - new_ind
                    cnt_list.append(a+b)
                else:
                    cnt_list.append(i)
        while index_list[-1] == 0:
            index_list.pop()
        cnt_list.append(len(index_list)-1)
        print(cnt_list)
        answer = sum(alphabet_list) + min(cnt_list)
    return answer