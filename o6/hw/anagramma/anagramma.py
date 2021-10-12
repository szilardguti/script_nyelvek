#!/usr/bin/env python3


def trivial_is_anagram(s1, s2):
    return sorted(normalize(s1)) == sorted(normalize(s2))
    
    
def not_so_trivial_is_anagram(s1, s2):
    d1 = {}
    d2 = {}
    for c in normalize(s1):
        if c not in d1:
            d1[c] = 0 
        d1[c] += 1
        
    for c in normalize(s2):
        if c not in d2:
            d2[c] = 0 
        d2[c] += 1
    
    for k in d1.keys():
        if k not in d2 or d1.get(k) != d2.get(k):
            return False
    return True
    

def normalize(s):
    return ''.join(s.split()).lower()


def main():
    print(trivial_is_anagram('listen', 'silent'))
    print(trivial_is_anagram('Clint Eastwood', 'Old west action'))
    print(trivial_is_anagram('nincs', 'nem van'))
    
    print("-"*15)
    
    print(not_so_trivial_is_anagram('listen', 'silent'))
    print(not_so_trivial_is_anagram('Clint Eastwood', 'Old west action'))
    print(not_so_trivial_is_anagram('nincs', 'nem van'))
    

if __name__ == "__main__":
    main()
