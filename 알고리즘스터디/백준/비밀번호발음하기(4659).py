vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def check_vowel_consonant(word, accept):
    for i in range(len(word)):
        if word[i] in vowels:
            accept = 1
            break
    
    vowel_count = 0
    consonant_count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_count += 1
            consonant_count = 0
            if vowel_count == 3:
                accept = 0
                break
        if word[i] in consonants:
            consonant_count += 1
            vowel_count = 0
            if consonant_count == 3:
                accept = 0
                break
    return accept

def check_same_alphabet(word, accept):
    for i in range(1, len(word)):
        if word[i] == 'e' or word[i] == 'o':
            continue
        else:
            if word[i] == word[i-1]:
                accept = 0
    return accept

while True:
    word = input()
    if word == 'end':
        break
    accept = 0
    accept = check_vowel_consonant(word, accept)
    # print(accept)
    accept = check_same_alphabet(word, accept)
    # print(accept)
    if accept == 1:
        print("<%s> is acceptable." % word)
    else:
        print("<%s> is not acceptable." % word)
    

        
    