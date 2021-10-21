#!/usr/bin/env python3


def is_valid_brackets(s):
    d = { ']' : '[', ')' : '(', '}' : '{' }
    pairs = []
    openings = []
    for c in s:
        if c in [ '[', '(', '{' ]:
            openings.append(c)
        elif c in [ ']', ')', '}' ]:
            if len(openings) != 0:
                pairs += list(zip(openings[-1], c))
                openings.remove(openings[-1])
            else: return False
    
    for o,e in pairs:
        if o != d[e]:
            return False
    if len(openings) == 0: return True
    else: return False
    

def main():
    print(is_valid_brackets("["))
    print(is_valid_brackets("((5+3)*2+1)"))
    print(is_valid_brackets("{[(3+1)+2]+}"))
    print(is_valid_brackets("(3+{1-1)}"))
    print(is_valid_brackets("[1+1]+(2*2)-{3/3}"))
    print(is_valid_brackets("(({[(((1)-2)+3)-3]/3}-3)"))


if __name__ == "__main__":
    main()
